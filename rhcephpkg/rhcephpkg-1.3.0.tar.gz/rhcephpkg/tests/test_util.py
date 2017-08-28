import os
import pytest
from rhcephpkg import util
from rhcephpkg.tests.util import CallRecorder

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_DIR = os.path.join(TESTS_DIR, 'fixtures')


class TestUtilCurrentBranch(object):

    def test_current_branch(self, testpkg, monkeypatch):
        assert util.current_branch() == 'ceph-2-ubuntu'

    def test_current_debian_branch(self, testpkg, monkeypatch):
        assert util.current_debian_branch() == 'ceph-2-ubuntu'

    def test_current_patches_branch(self, testpkg, monkeypatch):
        assert util.current_patches_branch() == 'patch-queue/ceph-2-ubuntu'


class TestUtilConfig(object):

    def test_missing_config_file(self, monkeypatch, tmpdir):
        # Set $HOME to a known-empty directory:
        monkeypatch.setenv('HOME', str(tmpdir))
        c = util.config()
        with pytest.raises(Exception):
            c.get('some.section', 'someoption')

    def test_working_config_file(self):
        c = util.config()
        assert c.get('rhcephpkg', 'user') == 'kdreyer'
        assert c.get('rhcephpkg', 'gitbaseurl') == \
            'ssh://%(user)s@git.example.com/ubuntu/%(module)s'
        assert c.get('rhcephpkg.jenkins', 'token') == \
            '5d41402abc4b2a76b9719d911017c592'
        assert c.get('rhcephpkg.jenkins', 'url') == \
            'https://ceph-jenkins.example.com/'
        assert c.get('rhcephpkg.chacra', 'url') == \
            'https://chacra.example.com/'


class TestUtilPackageName(object):

    def test_package_name(self, testpkg, monkeypatch):
        assert util.package_name() == 'testpkg'


class TestUtilChangelog(object):

    def test_format_changelog(self):
        """ test formatting a debian changelog """
        changes = ['a change', 'some other change', 'third change']
        expected = "  * a change\n  * some other change\n  * third change\n"
        assert util.format_changelog(changes) == expected

    def test_bump_changelog(self, testpkg, monkeypatch):
        """ test bumping a debian changelog """
        assert util.bump_changelog(['some change']) is True
        assert str(util.get_deb_version()) == '1.0.0-3redhat1'


class TestUtilDebVersion(object):
    @pytest.mark.parametrize('current,expected', [
        ('1.0.0-0redhat1', '1.0.0-1redhat1'),
        ('1.0.0-9redhat1', '1.0.0-10redhat1'),
        ('1.0.0-10redhat1', '1.0.0-11redhat1'),
        ('1.0.0-0.1redhat1', '1.0.0-0.2redhat1'),
        ('1.0.0-0.0.1redhat1', '1.0.0-0.0.2redhat1'),
        ('10.2.5-28.2.bz1464099redhat1', '10.2.5-28.3.bz1464099redhat1'),
        ('1.0.0-weird1redhat1', '1.0.0-weird1.1redhat1'),
    ])
    def test_next(self, current, expected):
        ver = util.DebVersion(current)
        nextver = ver.next()
        assert str(nextver) == expected


class TestUtilGetUserFullname(object):

    @pytest.fixture
    def setup(self, monkeypatch):
        class FakeGetpwuid(object):
            pw_gecos = 'Mr Gecos'
        monkeypatch.delenv('DEBFULLNAME', raising=False)
        monkeypatch.delenv('NAME', raising=False)
        monkeypatch.setattr('pwd.getpwuid', lambda uid: FakeGetpwuid())

    def test_debfullname_env(self, setup, monkeypatch):
        monkeypatch.setenv('DEBFULLNAME', 'Mr Deb Fullname')
        assert util.get_user_fullname() == 'Mr Deb Fullname'

    def test_name_env(self, setup, monkeypatch):
        monkeypatch.setenv('NAME', 'Mr Plain Name')
        assert util.get_user_fullname() == 'Mr Plain Name'

    def test_gecos(self, setup):
        assert util.get_user_fullname() == 'Mr Gecos'


class TestUtilSetupPristineTarBranch(object):

    def test_no_remote_branch(self, testpkg, monkeypatch):
        util.setup_pristine_tar_branch()
        assert not os.path.exists('.git/refs/heads/pristine-tar')

    def test_remote_branch_present(self, testpkg, monkeypatch):
        remotesdir = testpkg.join('.git').join('refs').mkdir('remotes')
        remotesdir.mkdir('origin').ensure('pristine-tar', file=True)
        recorder = CallRecorder()
        monkeypatch.setattr('subprocess.call', recorder)
        util.setup_pristine_tar_branch()
        expected = ['git', 'branch', '--track', 'pristine-tar',
                    'origin/pristine-tar']
        assert recorder.args == expected

    def test_remote_and_local_branches_present(self, testpkg, monkeypatch):
        refsdir = testpkg.join('.git').join('refs')
        refsdir.mkdir('remotes').mkdir('origin').ensure('pristine-tar',
                                                        file=True)
        refsdir.join('heads').ensure('pristine-tar', file=True)
        recorder = CallRecorder()
        monkeypatch.setattr('subprocess.call', recorder)
        util.setup_pristine_tar_branch()
        assert recorder.called == 0
