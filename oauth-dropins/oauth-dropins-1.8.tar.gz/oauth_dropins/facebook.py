"""Facebook OAuth drop-in.

https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow

TODO: implement client state param
TODO: unify this with instagram. see file docstring comment there.
"""

import json
import logging
import urllib
import urllib2
import urlparse
from webob import exc

import appengine_config
from appengine_config import HTTP_TIMEOUT
import handlers
import models
from webutil import util

from google.appengine.ext import ndb


API_BASE = 'https://graph.facebook.com/v2.10/'

# facebook api url templates. can't (easily) use urllib.urlencode() because i
# want to keep the %(...)s placeholders as is and fill them in later in code.
# https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow#logindialog
GET_AUTH_CODE_URL = str('&'.join((
    'https://www.facebook.com/v2.10/dialog/oauth?'
    # https://developers.facebook.com/docs/reference/login/
    'scope=%(scope)s',
    'client_id=%(client_id)s',
    # redirect_uri here must be the same in the access token request!
    'redirect_uri=%(redirect_uri)s',
    'response_type=code',
    )))
# https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow#exchangecode
GET_ACCESS_TOKEN_URL = str('&'.join((
    API_BASE + 'oauth/access_token?'
    'client_id=%(client_id)s',
    # redirect_uri here must be the same in the oauth request!
    # (the value here doesn't actually matter since it's requested server side.)
    'redirect_uri=%(redirect_uri)s',
    'client_secret=%(client_secret)s',
    'code=%(auth_code)s',
    )))
API_USER_URL = API_BASE + 'me?fields=id,about,cover,email,gender,link,location,name,public_key,timezone,updated_time,website'
API_PAGE_URL = API_BASE + 'me?fields=id,about,cover,description,emails,general_info,is_published,link,location,name,personal_info,phone,username,website'
API_PAGES_URL = API_BASE + 'me/accounts'


class FacebookAuth(models.BaseAuth):
  """An authenticated Facebook user or page.

  Provides methods that return information about this user (or page) and make
  OAuth-signed requests to Facebook's HTTP-based APIs. Stores OAuth credentials
  in the datastore. See models.BaseAuth for usage details.

  Facebook-specific details: implements urlopen() but not http() or api(). The
  key name is the user's or page's Facebook ID.
  """
  type = ndb.StringProperty(choices=('user', 'page'))
  auth_code = ndb.StringProperty()
  access_token_str = ndb.StringProperty(required=True)
  # https://developers.facebook.com/docs/graph-api/reference/user#fields
  user_json = ndb.TextProperty(required=True)
  # https://developers.facebook.com/docs/graph-api/reference/user/accounts#fields
  pages_json = ndb.TextProperty()

  def site_name(self):
    return 'Facebook'

  def user_display_name(self):
    """Returns the user's or page's name.
    """
    return json.loads(self.user_json)['name']

  def access_token(self):
    """Returns the OAuth access token string.
    """
    return self.access_token_str

  def urlopen(self, url, **kwargs):
    """Wraps urllib2.urlopen() and adds OAuth credentials to the request.
    """
    return models.BaseAuth.urlopen_access_token(url, self.access_token_str,
                                                **kwargs)

  def for_page(self, page_id):
    """Returns a new, unsaved FacebookAuth entity for a page in pages_json.

    The returned entity's properties will be populated with the page's data.
    access_token will be the page access token, user_json will be the page
    object, and pages_json will be a single-element list with the page.

    If page_id is not in pages_json, returns None.

    Args:
      page_id: string, Facebook page id
    """
    for page in json.loads(self.pages_json):
      id = page.get('id')
      if id == page_id:
        entity = FacebookAuth(id=id, type='page', pages_json=json.dumps([page]),
                              access_token_str=page.get('access_token'))
        entity.user_json = entity.urlopen(API_PAGE_URL).read()
        logging.debug('Page object: %s', entity.user_json)
        return entity

    return None

  def is_authority_for(self, key):
    """Additionally check if the key represents a Page that this user has
    authority over.

    Args:
      auth_entity_key: ndb.Key

    Returns:
      boolean: true if key represents this user or one of the user's pages.
    """
    return super(FacebookAuth, self).is_authority_for(key) or any(
      key == self.for_page(page.get('id')).key
      for page in json.loads(self.pages_json))


class StartHandler(handlers.StartHandler):
  """Starts Facebook auth. Requests an auth code and expects a redirect back.
  """

  def redirect_url(self, state=None, app_id=None):
    if app_id is None:
      assert (appengine_config.FACEBOOK_APP_ID and
              appengine_config.FACEBOOK_APP_SECRET), (
              "Please fill in the facebook_app_id and facebook_app_secret files"
              " in your app's root directory.")
      app_id = appengine_config.FACEBOOK_APP_ID

    return str(GET_AUTH_CODE_URL % {
      'client_id': app_id,
      'scope': self.scope,
      # TODO: CSRF protection identifier.
      # http://developers.facebook.com/docs/authentication/
      'redirect_uri': urllib.quote_plus(self.to_url(state=state)),
      })


class CallbackHandler(handlers.CallbackHandler):
  """The auth callback. Fetches an access token, stores it, and redirects home.
  """

  def get(self):
    if CallbackHandler.handle_error(self):
      return

    auth_code = util.get_required_param(self, 'code')
    url = GET_ACCESS_TOKEN_URL % {
      'auth_code': auth_code,
      'client_id': appengine_config.FACEBOOK_APP_ID,
      'client_secret': appengine_config.FACEBOOK_APP_SECRET,
      'redirect_uri': urllib.quote_plus(self.request_url_with_state()),
      }
    try:
      resp = json.loads(util.urlopen(url).read())
    except urllib2.HTTPError, e:
      logging.error(e.read())
      raise

    logging.debug('Access token response: %s', resp)
    access_token = resp['access_token']

    user = models.BaseAuth.urlopen_access_token(API_USER_URL, access_token).read()
    logging.debug('User info response: %s', user)
    user_id = json.loads(user)['id']

    pages = json.dumps(json.loads(models.BaseAuth.urlopen_access_token(
      API_PAGES_URL, access_token).read()).get('data'))
    logging.debug('Pages response: %s', pages)

    auth = FacebookAuth(id=user_id,
                        type='user',
                        user_json=user,
                        pages_json=pages,
                        auth_code=auth_code,
                        access_token_str=access_token)
    auth.put()
    self.finish(auth, state=self.request.get('state'))

  @staticmethod
  def handle_error(handler):
    """Handles any error reported in the callback query parameters.

    Args:
      handler: CallbackHandler

    Returns:
      True if there was an error, False otherwise.
    """
    error = handler.request.get('error')
    error_reason = handler.request.get('error_reason')

    if error or error_reason:
      error_description = urllib.unquote_plus(
        handler.request.get('error_description', ''))
      if error == 'access_denied' and error_reason == 'user_denied':
        logging.info('User declined: %s', error_description)
        handler.finish(None, state=handler.request.get('state'))
        return True
      else:
        raise exc.HTTPBadRequest(' '.join((error, error_reason, error_description)))

    return False
