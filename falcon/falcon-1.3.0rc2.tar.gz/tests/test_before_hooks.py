import functools
import io

import pytest

try:
    import ujson as json
except ImportError:
    import json

import falcon
import falcon.testing as testing


def validate(req, resp, params):
    raise falcon.HTTPBadRequest('Invalid thing', 'Your thing was not '
                                'formatted correctly.')


def validate_param(req, resp, params):
    limit = req.get_param_as_int('limit')
    if limit and int(limit) > 100:
        raise falcon.HTTPBadRequest('Out of range', 'limit must be <= 100')


def resource_aware_validate_param(req, resp, resource, params):
    assert resource
    validate_param(req, resp, params)


class ResourceAwareValidateParam(object):
    def __call__(self, req, resp, resource, params):
        assert resource
        validate_param(req, resp, params)


def validate_field(req, resp, params):
    try:
        params['id'] = int(params['id'])
    except ValueError:
        raise falcon.HTTPBadRequest('Invalid ID', 'ID was not valid.')


def parse_body(req, resp, params):
    length = req.content_length or 0
    if length != 0:
        params['doc'] = json.load(io.TextIOWrapper(req.stream, 'utf-8'))


def bunnies(req, resp, params):
    params['bunnies'] = 'fuzzy'


def resource_aware_bunnies(req, resp, resource, params):
    assert resource
    bunnies(req, resp, params)


def frogs(req, resp, params):
    if 'bunnies' in params:
        params['bunnies'] = 'fluffy'

    params['frogs'] = 'not fluffy'


class Fish(object):
    def __call__(self, req, resp, params):
        params['fish'] = 'slippery'

    def hook(self, req, resp, resource, params):
        params['fish'] = 'wet'


# NOTE(kgriffs): Use partial methods for these next two in order
# to make sure we handle that correctly.
def things_in_the_head(header, value, req, resp, resource, params):
    resp.set_header(header, value)


bunnies_in_the_head = functools.partial(
    things_in_the_head,
    'X-Bunnies',
    'fluffy'
)

frogs_in_the_head = functools.partial(
    things_in_the_head,
    'X-Frogs',
    'not fluffy'
)


class WrappedRespondersResource(object):

    @falcon.before(validate_param)
    @falcon.before(parse_body)
    def on_get(self, req, resp, doc):
        self.req = req
        self.resp = resp
        self.doc = doc

    @falcon.before(validate)
    def on_put(self, req, resp):
        self.req = req
        self.resp = resp


@falcon.before(bunnies)
class WrappedClassResource(object):

    _some_fish = Fish()

    # Test non-callable should be skipped by decorator
    on_patch = {}

    @falcon.before(validate_param)
    def on_get(self, req, resp, bunnies):
        self._capture(req, resp, bunnies)

    @falcon.before(validate_param)
    def on_head(self, req, resp, bunnies):
        self._capture(req, resp, bunnies)

    @falcon.before(_some_fish)
    def on_post(self, req, resp, fish, bunnies):
        self._capture(req, resp, bunnies)
        self.fish = fish

    @falcon.before(_some_fish.hook)
    def on_put(self, req, resp, fish, bunnies):
        self._capture(req, resp, bunnies)
        self.fish = fish

    def _capture(self, req, resp, bunnies):
        self.req = req
        self.resp = resp
        self.bunnies = bunnies


# NOTE(swistakm): we both both type of hooks (class and method)
# at once for the sake of simplicity
@falcon.before(resource_aware_bunnies)
class ClassResourceWithAwareHooks(object):
    hook_as_class = ResourceAwareValidateParam()

    @falcon.before(resource_aware_validate_param)
    def on_get(self, req, resp, bunnies):
        self._capture(req, resp, bunnies)

    @falcon.before(resource_aware_validate_param)
    def on_head(self, req, resp, bunnies):
        self._capture(req, resp, bunnies)

    @falcon.before(hook_as_class)
    def on_put(self, req, resp, bunnies):
        self._capture(req, resp, bunnies)

    @falcon.before(hook_as_class.__call__)
    def on_post(self, req, resp, bunnies):
        self._capture(req, resp, bunnies)

    def _capture(self, req, resp, bunnies):
        self.req = req
        self.resp = resp
        self.bunnies = bunnies


class TestFieldResource(object):

    @falcon.before(validate_field)
    def on_get(self, req, resp, id):
        self.id = id


@falcon.before(bunnies)
@falcon.before(frogs)
@falcon.before(Fish())
@falcon.before(bunnies_in_the_head)
@falcon.before(frogs_in_the_head)
class ZooResource(object):

    def on_get(self, req, resp, bunnies, frogs, fish):
        self.bunnies = bunnies
        self.frogs = frogs
        self.fish = fish


@pytest.fixture
def wrapped_aware_resource():
    return ClassResourceWithAwareHooks()


@pytest.fixture
def wrapped_resource():
    return WrappedClassResource()


@pytest.fixture
def field_resource():
    return TestFieldResource()


@pytest.fixture
def resource():
    return WrappedRespondersResource()


@pytest.fixture
def client(resource):
    app = falcon.API()
    app.add_route('/', resource)
    return testing.TestClient(app)


def test_multiple_resource_hooks(client):
    zoo_resource = ZooResource()
    client.app.add_route('/', zoo_resource)

    result = client.simulate_get('/')

    assert 'not fluffy' == result.headers['X-Frogs']
    assert 'fluffy' == result.headers['X-Bunnies']

    assert 'fluffy' == zoo_resource.bunnies
    assert 'not fluffy' == zoo_resource.frogs
    assert 'slippery' == zoo_resource.fish


def test_input_validator(client):
    result = client.simulate_put('/')
    assert result.status_code == 400


def test_param_validator(client):
    result = client.simulate_get('/', query_string='limit=10', body='{}')
    assert result.status_code == 200

    result = client.simulate_get('/', query_string='limit=101')
    assert result.status_code == 400


def test_field_validator(client, field_resource):
    client.app.add_route('/queue/{id}/messages', field_resource)
    result = client.simulate_get('/queue/10/messages')
    assert result.status_code == 200
    assert field_resource.id == 10

    result = client.simulate_get('/queue/bogus/messages')
    assert result.status_code == 400


def test_parser(client, resource):
    client.simulate_get('/', body=json.dumps({'animal': 'falcon'}))
    assert resource.doc == {'animal': 'falcon'}


def test_wrapped_resource(client, wrapped_resource):
    client.app.add_route('/wrapped', wrapped_resource)
    result = client.simulate_patch('/wrapped')
    assert result.status_code == 405

    result = client.simulate_get('/wrapped', query_string='limit=10')
    assert result.status_code == 200
    assert 'fuzzy' == wrapped_resource.bunnies

    result = client.simulate_head('/wrapped')
    assert result.status_code == 200
    assert 'fuzzy' == wrapped_resource.bunnies

    result = client.simulate_post('/wrapped')
    assert result.status_code == 200
    assert 'slippery' == wrapped_resource.fish

    result = client.simulate_get('/wrapped', query_string='limit=101')
    assert result.status_code == 400
    assert wrapped_resource.bunnies == 'fuzzy'


def test_wrapped_resource_with_hooks_aware_of_resource(client, wrapped_aware_resource):
    client.app.add_route('/wrapped_aware', wrapped_aware_resource)

    result = client.simulate_patch('/wrapped_aware')
    assert result.status_code == 405

    result = client.simulate_get('/wrapped_aware', query_string='limit=10')
    assert result.status_code == 200
    assert wrapped_aware_resource.bunnies == 'fuzzy'

    for method in ('HEAD', 'PUT', 'POST'):
        result = client.simulate_request(method, '/wrapped_aware')
        assert result.status_code == 200
        assert wrapped_aware_resource.bunnies == 'fuzzy'

    result = client.simulate_get('/wrapped_aware', query_string='limit=101')
    assert result.status_code == 400
    assert wrapped_aware_resource.bunnies == 'fuzzy'
