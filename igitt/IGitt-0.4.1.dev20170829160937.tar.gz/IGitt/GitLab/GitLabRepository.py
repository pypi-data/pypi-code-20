"""
Contains the GitLab Repository implementation.
"""
from datetime import datetime
from urllib.parse import quote_plus

from IGitt import ElementAlreadyExistsError, ElementDoesntExistError
from IGitt.GitLab import delete, get, post, GitLabMixin
from IGitt.GitLab import GitLabOAuthToken, GitLabPrivateToken
from IGitt.GitLab.GitLabIssue import GitLabIssue
from IGitt.Interfaces.Repository import Repository
from IGitt.Interfaces.Repository import WebhookEvents
from IGitt.Utils import eliminate_none

GL_WEBHOOK_TRANSLATION = {
    WebhookEvents.PUSH: 'push_events',
    WebhookEvents.ISSUE: 'issues_events',
    WebhookEvents.MERGE_REQUEST: 'merge_requests_events',
    WebhookEvents.COMMIT_COMMENT: 'note_events',
    WebhookEvents.MERGE_REQUEST_COMMENT: 'note_events',
    WebhookEvents.ISSUE_COMMENT: 'note_events',
}

GL_WEBHOOK_EVENTS = {'tag_push_events', 'job_events', 'pipeline_events',
                     'wiki_events'} | set(GL_WEBHOOK_TRANSLATION.values())

def date_in_range(data,
                  created_after='',
                  created_before='',
                  updated_after='',
                  updated_before=''):
    """
    Returns true if issue/MR is in the given range.
    """
    is_created_after = not created_after
    is_created_before = not created_before
    is_updated_after = not updated_after
    is_updated_before = not updated_before
    if created_after and data['created_at']>str(created_after):
        is_created_after = True
    if created_before and data['created_at']<str(created_before):
        is_created_before = True
    if updated_after and data['updated_at']>str(updated_after):
        is_updated_after = True
    if updated_before and data['updated_at']<str(updated_before):
        is_updated_before = True
    return (is_created_after and is_created_before and is_updated_after and
            is_updated_before)

class GitLabRepository(Repository, GitLabMixin):
    """
    Represents a repository on GitLab.
    """

    def __init__(self, token: (GitLabOAuthToken, GitLabPrivateToken),
                 repository: str):
        """
        Creates a new GitLabRepository object with the given credentials.

        :param token: A Token object to be used for authentication.
        :param repository: The full name of the repository,
                           e.g. ``sils/baritone``.
        """
        self._token = token
        self._repository = repository
        self._url = '/projects/' + quote_plus(repository)

    @property
    def hoster(self) -> str:
        """
        Indicates that the repository is hosted by GitLab.

        :return: "gitlab".
        """
        return 'gitlab'  # dont cover

    @property
    def full_name(self) -> str:
        """
        Retrieves the full name of the repository, e.g. "sils/baritone".

        >>> from os import environ
        >>> repo = GitLabRepository(
        ...     GitLabOAuthToken(environ['GITLAB_TEST_TOKEN']),
        ...     'gitmate-test-user/test'
        ... )
        >>> repo.full_name
        'gitmate-test-user/test'

        :return: The full repository name as string.
        """
        if self._repository.isdigit():
            self._repository = self.data['path_with_namespace']
        return self._repository

    @property
    def clone_url(self) -> str:
        """
        Retrieves the URL of the repository.

        >>> from os import environ as env
        >>> repo = GitLabRepository(
        ...     GitLabOAuthToken(environ['GITLAB_TEST_TOKEN']),
        ...     'gitmate-test-user/test'
        ... )
        >>> expected = 'https://{}@gitlab.com/gitmate-test-user/test.git'
        >>> assert repo.clone_url == expected.format(env['GITLAB_TEST_TOKEN'])

        :return: A URL that can be used to clone the repository with Git.
        """
        return self.data['http_url_to_repo'].replace(
            '://', '://oauth2:' + self._token.value + '@', 1)

    def get_labels(self) -> {str}:
        """
        Retrieves the labels of the repository.

        >>> from os import environ
        >>> repo = GitLabRepository(
        ...     GitLabOAuthToken(environ['GITLAB_TEST_TOKEN']),
        ...     'gitmate-test-user/test'
        ... )
        >>> sorted(repo.get_labels())
        ['a', 'b', 'c']

        :return: A set of strings containing the label captions.
        """
        return {label['name']
                for label in get(self._token, self._url + '/labels')}

    def create_label(self, name: str, color: str):
        """
        Creates a new label with the given color. For an example,
        see delete_label.

        If a label that already exists is attempted to be created, that throws
        an exception:

        >>> from os import environ
        >>> repo = GitLabRepository(
        ...     GitLabOAuthToken(environ['GITLAB_TEST_TOKEN']),
        ...     'gitmate-test-user/test'
        ... )
        >>> sorted(repo.get_labels())
        ['a', 'b', 'c']
        >>> repo.create_label('c', '#555555')
        Traceback (most recent call last):
         ...
        IGitt.ElementAlreadyExistsError: c already exists.

        :param name: The name of the label to create.
        :param color: A HTML color value with a leading #.
        :raises ElementAlreadyExistsError: If the label name already exists.
        :raises RuntimeError: If something goes wrong (network, auth...).
        """
        if name in self.get_labels():
            raise ElementAlreadyExistsError(name + ' already exists.')

        self.data = post(
            self._token,
            self._url + '/labels',
            {'name': name, 'color': color}
        )

    def delete_label(self, name: str):
        """
        Deletes a label.

        Take a given repository:

        >>> from os import environ
        >>> repo = GitLabRepository(
        ...     GitLabOAuthToken(environ['GITLAB_TEST_TOKEN']),
        ...     'gitmate-test-user/test'
        ... )
        >>> sorted(repo.get_labels())
        ['a', 'b', 'c']

        Let's create a label 'd':

        >>> repo.create_label('d', '#555555')
        >>> sorted(repo.get_labels())
        ['a', 'b', 'c', 'd']

        >>> repo.delete_label('d')
        >>> sorted(repo.get_labels())
        ['a', 'b', 'c']

        If the label doesn't exist it won't get silently dropped - no! You will
        get an exception.

        >>> repo.delete_label('d')
        Traceback (most recent call last):
         ...
        IGitt.ElementDoesntExistError: d doesnt exist.

        :param name: The caption of the label to delete.
        :raises ElementDoesntExistError: If the label doesn't exist.
        :raises RuntimeError: If something goes wrong (network, auth...).
        """
        if name not in self.get_labels():
            raise ElementDoesntExistError(name + ' doesnt exist.')

        delete(self._token, self._url + '/labels', {'name': name})

    def get_issue(self, issue_number: int) -> GitLabIssue:
        """
        Retrieves an issue:

        >>> from os import environ
        >>> repo = GitLabRepository(
        ...     GitLabOAuthToken(environ['GITLAB_TEST_TOKEN']),
        ...     'gitmate-test-user/test'
        ... )
        >>> repo.get_issue(1).title
        'Take it serious, son!'

        :param issue_number: The issue IID of the issue on GitLab.
        :return: An Issue object.
        :raises ElementDoesntExistError: If the issue doesn't exist.
        :raises RuntimeError: If something goes wrong (network, auth...).
        """
        return GitLabIssue(self._token, self.full_name, issue_number)

    def get_mr(self, mr_number: int):
        """
        Retrieves an MR.

        :param mr_number: The MR IID of the merge_request on GitLab.
        :return: A MergeRequest object.
        :raises ElementDoesntExistError: If the MR doesn't exist.
        :raises RuntimeError: If something goes wrong (network, auth...).
        """
        from IGitt.GitLab.GitLabMergeRequest import GitLabMergeRequest
        return GitLabMergeRequest(self._token, self.full_name, mr_number)

    @property
    def hooks(self) -> {str}:
        """
        Retrieves all URLs this repository is hooked to.

        :return: Set of URLs (str).
        """
        hook_url = self._url + '/hooks'
        hooks = get(self._token, hook_url)

        return {hook['url'] for hook in hooks}

    def register_hook(self,
                      url: str,
                      secret: str=None,
                      events: {WebhookEvents}=None):
        """
        Registers a webhook to the given URL. Use it as simple as:

        >>> from os import environ
        >>> repo = GitLabRepository(environ['GITLAB_TEST_TOKEN'],
        ...                         'gitmate-test-user/test')
        >>> repo.register_hook("http://some.url/in/the/world")

        It does nothing if the hook is already there:

        >>> repo.register_hook("http://some.url/in/the/world")

        To register a secret token with the webhook, simply add
        the secret param:

        >>> repo.register_hook("http://some.url/i/have/a/secret",
        ...     "mylittlesecret")

        To delete it simply run:

        >>> repo.delete_hook("http://some.url/in/the/world")
        >>> repo.delete_hook("http://some.url/i/have/a/secret")

        :param url: The URL to fire the webhook to.
        :param secret:
            An optional secret token to be registered with the webhook.
        :param events:
            The events for which the webhook is to be registered against.
            Defaults to all possible events.
        :raises RuntimeError: If something goes wrong (network, auth...).
        """
        if url in self.hooks:
            return

        config = {
            'url': url,
            'enable_ssl_verification': False,
        }

        if secret:
            config['token'] = secret

        if events and len(events):
            config.update({GL_WEBHOOK_TRANSLATION[event]: True
                           for event in events})
        else:
            config.update({event: True for event in GL_WEBHOOK_EVENTS})

        self.data = post(self._token, self._url + '/hooks', config)

    def delete_hook(self, url: str):
        """
        Deletes all webhooks to the given URL.

        :param url: The URL to not fire the webhook to anymore.
        :raises RuntimeError: If something goes wrong (network, auth...).
        """
        hook_url = self._url + '/hooks'
        hooks = get(self._token, hook_url)

        # Do not use self.hooks since id of the hook is needed
        for hook in hooks:
            if hook['url'] == url:
                delete(self._token, hook_url + '/' + str(hook['id']))

    def create_issue(self, title: str, body: str='') -> GitLabIssue:
        """
        Create a new issue in the repository.
        """
        return GitLabIssue.create(self._token, self.full_name, title, body)

    @property
    def merge_requests(self) -> set:
        """
        Retrieves a set of merge request objects.

        >>> from os import environ
        >>> repo = GitLabRepository(
        ...     GitLabOAuthToken(environ['GITLAB_TEST_TOKEN']),
        ...     'gitmate-test-user/test'
        ... )
        >>> len(repo.merge_requests)
        4
        """
        from IGitt.GitLab.GitLabMergeRequest import GitLabMergeRequest
        return {GitLabMergeRequest.from_data(res, self._token,
                                             self.full_name, res['iid'])
                for res in get(self._token, self._url + '/merge_requests')}

    def filter_issues(self, state: str='opened') -> set:
        """
        Filters the issues from the repository based on properties.

        :param state: 'opened' or 'closed' or 'all'.
        """
        params = {'state': state}
        return {GitLabIssue.from_data(res, self._token,
                                      self.full_name, res['iid'])
                for res in get(self._token, self._url + '/issues', params)}

    @property
    def issues(self) -> set:
        """
        Retrieves a set of issue objects.

        >>> from os import environ
        >>> repo = GitLabRepository(environ['GITLAB_TEST_TOKEN'],
        ...                         'gitmate-test-user/test')
        >>> len(repo.issues)
        13
        """
        return self.filter_issues()

    def create_fork(self, organization: (str, None)=None,
                    namespace: (str, None)=None):
        """
        Create a fork of Repository
        """
        url = self._url + '/fork'
        data = {
            'id': self._repository,
            'namespace': namespace
        }
        res = post(self._token, url=url, data=data)

        return GitLabRepository(self._token, res['path_with_namespace'])

    def create_file(self, path: str, message: str, content: str,
                    branch: (str, None)=None, committer:(str, None)=None,
                    author:(dict, None)=None, encoding:(str, None)=None):
        """
        Create a new file in Repository
        """
        url = self._url + '/repository/files/' + path
        data = {
            'file_path' : path,
            'commit_message' : message,
            'content' : content,
            'branch' : branch,
            'encoding' : encoding
        }

        if author:
            data['author_name'] = author['name']
            data['author_email'] = author['email']

        data = eliminate_none(data)
        post(token=self._token, url=url, data=data)

        from IGitt.GitLab.GitLabContent import GitLabContent
        return GitLabContent(self._token, self._repository, path=path)

    def create_merge_request(self, title:str, base:str, head:str,
                             body: (str, None)=None,
                             target_project_id: (int, None)=None,
                             target_project: (str, None)=None):
        """
        Create a new merge request in Repository
        """
        url = self._url + '/merge_requests'
        data = {
            'title' : title,
            'target_branch' : base,
            'source_branch' : head,
            'id' : quote_plus(self._repository),
            'target_project_id' : target_project_id
        }
        json = post(self._token, url=url, data=data)

        from IGitt.GitLab.GitLabMergeRequest import GitLabMergeRequest
        return GitLabMergeRequest.from_data(json, self._token,
                                            repository=target_project,
                                            number=json['iid'])

    def delete(self):
        """
        Delete the Repository
        """
        delete(token=self._token, url=self._url)

    def _search(self,
                search_type):
        """
        Retrives a list of all open issues or merge requests.
        :param search_type: A string for type of object i.e. issues for issue
                            and merge_requests for merge requests.
        :return: List of issues/merge requests.
        """
        query = dict()
        url = self._url + '/{}'.format(search_type)
        query['state'] = 'opened'
        return get(self._token, url, params=query)


    def search_issues(self,
                      created_after: datetime='',
                      created_before: datetime='',
                      updated_after: datetime='',
                      updated_before: datetime=''):
        """
        Searches for issues based on created and updated date.
        """
        for issue_data in filter(lambda data: date_in_range(data,
                                                            created_after,
                                                            created_before,
                                                            updated_after,
                                                            updated_before),
                                 self._search('issues')):
            issue = self.get_issue(issue_data['iid'])
            issue.data = issue_data
            yield issue

    def search_mrs(self,
                   created_after: datetime='',
                   created_before: datetime='',
                   updated_after: datetime='',
                   updated_before: datetime=''):
        """
        Searches for merge request based on created and updated date.
        """
        for mr_data in filter(lambda data: date_in_range(data,
                                                         created_after,
                                                         created_before,
                                                         updated_after,
                                                         updated_before),
                              self._search('merge_requests')):
            merge_request = self.get_mr(mr_data['iid'])
            merge_request.data = mr_data
            yield merge_request
