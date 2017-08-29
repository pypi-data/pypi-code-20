import glob
import gzip
import logging
import os
import re
import shutil
import subprocess

from autotest.client import utils
from autotest.client.shared import log, software_manager, utils_memory
from autotest.client.shared.settings import settings

_LOG_INSTALLED_PACKAGES = settings.get_value('CLIENT', 'log_installed_packages',
                                             type=bool, default=False)

_DEFAULT_COMMANDS_TO_LOG_PER_TEST = []
_DEFAULT_COMMANDS_TO_LOG_PER_BOOT = [
    "lspci -vvnn", "gcc --version", "ld --version", "mount", "hostname",
    "uptime", "dmidecode", "ifconfig -a", "brctl show", "ip link",
    "numactl --hardware show", "lscpu", "fdisk -l",
]
_DEFAULT_COMMANDS_TO_LOG_BEFORE_ITERATION = []
_DEFAULT_COMMANDS_TO_LOG_AFTER_ITERATION = []

_DEFAULT_FILES_TO_LOG_PER_TEST = []
_DEFAULT_FILES_TO_LOG_PER_BOOT = [
    "/proc/pci", "/proc/meminfo", "/proc/slabinfo", "/proc/version",
    "/proc/cpuinfo", "/proc/modules", "/proc/interrupts", "/proc/partitions",
    "/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor",
    "/sys/kernel/debug/sched_features",
    "/sys/devices/system/clocksource/clocksource0/current_clocksource"
]
_DEFAULT_FILES_TO_LOG_BEFORE_ITERATION = [
    "/proc/schedstat", "/proc/meminfo", "/proc/slabinfo", "/proc/interrupts",
    "/proc/buddyinfo"
]
_DEFAULT_FILES_TO_LOG_AFTER_ITERATION = [
    "/proc/schedstat", "/proc/meminfo", "/proc/slabinfo", "/proc/interrupts",
    "/proc/buddyinfo"
]


class loggable(object):

    """ Abstract class for representing all things "loggable" by sysinfo. """

    def __init__(self, logf, log_in_keyval):
        self.logf = logf
        self.log_in_keyval = log_in_keyval

    def readline(self, logdir):
        path = os.path.join(logdir, self.logf)
        if os.path.exists(path):
            return utils.read_one_line(path)
        else:
            return ""


class logfile(loggable):

    def __init__(self, path, logf=None, log_in_keyval=False):
        if not logf:
            logf = os.path.basename(path)
        super(logfile, self).__init__(logf, log_in_keyval)
        self.path = path

    def __repr__(self):
        r = "sysinfo.logfile(%r, %r, %r)"
        r %= (self.path, self.logf, self.log_in_keyval)
        return r

    def __eq__(self, other):
        if isinstance(other, logfile):
            return (self.path, self.logf) == (other.path, other.logf)
        elif isinstance(other, loggable):
            return False
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def __hash__(self):
        return hash((self.path, self.logf))

    def run(self, logdir):
        if os.path.exists(self.path):
            try:
                shutil.copyfile(self.path, os.path.join(logdir, self.logf))
            except IOError:
                logging.info("Not logging %s (lack of permissions)",
                             self.path)


class command(loggable):

    def __init__(self, cmd, logf=None, log_in_keyval=False, compress_log=False):
        if not logf:
            logf = cmd.replace(" ", "_")
        super(command, self).__init__(logf, log_in_keyval)
        self.cmd = cmd
        self._compress_log = compress_log

    def __repr__(self):
        r = "sysinfo.command(%r, %r, %r)"
        r %= (self.cmd, self.logf, self.log_in_keyval)
        return r

    def __eq__(self, other):
        if isinstance(other, command):
            return (self.cmd, self.logf) == (other.cmd, other.logf)
        elif isinstance(other, loggable):
            return False
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def __hash__(self):
        return hash((self.cmd, self.logf))

    def run(self, logdir):
        env = os.environ.copy()
        if "PATH" not in env:
            env["PATH"] = "/usr/bin:/bin"
        logf_path = os.path.join(logdir, self.logf)
        stdin = open(os.devnull, "r")
        stderr = open(os.devnull, "w")
        stdout = open(logf_path, "w")
        try:
            subprocess.call(self.cmd, stdin=stdin, stdout=stdout, stderr=stderr,
                            shell=True, env=env)
        finally:
            for f in (stdin, stdout, stderr):
                f.close()
            if self._compress_log and os.path.exists(logf_path):
                utils.run('gzip -9 "%s"' % logf_path, ignore_status=True,
                          verbose=False)


class base_sysinfo(object):

    def __init__(self, job_resultsdir):
        self.sysinfodir = self._get_sysinfodir(job_resultsdir)

        # pull in the post-test logs to collect
        self.test_loggables = set()
        for cmd in _DEFAULT_COMMANDS_TO_LOG_PER_TEST:
            self.test_loggables.add(command(cmd))
        for filename in _DEFAULT_FILES_TO_LOG_PER_TEST:
            self.test_loggables.add(logfile(filename))

        # pull in the EXTRA post-boot logs to collect
        self.boot_loggables = set()
        for cmd in _DEFAULT_COMMANDS_TO_LOG_PER_BOOT:
            self.boot_loggables.add(command(cmd))
        for filename in _DEFAULT_FILES_TO_LOG_PER_BOOT:
            self.boot_loggables.add(logfile(filename))

        # pull in the pre test iteration logs to collect
        self.before_iteration_loggables = set()
        for cmd in _DEFAULT_COMMANDS_TO_LOG_BEFORE_ITERATION:
            self.before_iteration_loggables.add(
                command(cmd, logf=cmd.replace(" ", "_") + '.before'))
        for fname in _DEFAULT_FILES_TO_LOG_BEFORE_ITERATION:
            self.before_iteration_loggables.add(
                logfile(fname, logf=os.path.basename(fname) + '.before'))

        # pull in the post test iteration logs to collect
        self.after_iteration_loggables = set()
        for cmd in _DEFAULT_COMMANDS_TO_LOG_AFTER_ITERATION:
            self.after_iteration_loggables.add(
                command(cmd, logf=cmd.replace(" ", "_") + '.after'))
        for fname in _DEFAULT_FILES_TO_LOG_AFTER_ITERATION:
            self.after_iteration_loggables.add(
                logfile(fname, logf=os.path.basename(fname) + '.after'))

        # add in a couple of extra files and commands we want to grab
        self.test_loggables.add(command("df -mP", logf="df"))
        # We compress the dmesg because it can get large when kernels are
        # configured with a large buffer and some tests trigger OOMs or
        # other large "spam" that fill it up...
        self.test_loggables.add(command("dmesg -c", logf="dmesg",
                                        compress_log=True))
        self.boot_loggables.add(logfile("/proc/cmdline",
                                        log_in_keyval=True))
        # log /proc/mounts but with custom filename since we already
        # log the output of the "mount" command as the filename "mount"
        self.boot_loggables.add(logfile('/proc/mounts', logf='proc_mounts'))
        self.boot_loggables.add(command("uname -a", logf="uname",
                                        log_in_keyval=True))
        self.sm = software_manager.SoftwareManager()

    def __getstate__(self):
        ret = dict(self.__dict__)
        ret["sm"] = None
        return ret

    def serialize(self):
        return {"boot": self.boot_loggables, "test": self.test_loggables}

    def deserialize(self, serialized):
        self.boot_loggables = serialized["boot"]
        self.test_loggables = serialized["test"]

    @staticmethod
    def _get_sysinfodir(resultsdir):
        sysinfodir = os.path.join(resultsdir, "sysinfo")
        if not os.path.exists(sysinfodir):
            os.makedirs(sysinfodir)
        return sysinfodir

    def _get_reboot_count(self):
        if not glob.glob(os.path.join(self.sysinfodir, "*")):
            return -1
        else:
            return len(glob.glob(os.path.join(self.sysinfodir, "boot.*")))

    def _get_boot_subdir(self, next=False):
        reboot_count = self._get_reboot_count()
        if next:
            reboot_count += 1
        if reboot_count < 1:
            return self.sysinfodir
        else:
            boot_dir = "boot.%d" % (reboot_count - 1)
            return os.path.join(self.sysinfodir, boot_dir)

    def _get_iteration_subdir(self, test, iteration):
        iter_dir = "iteration.%d" % iteration

        logdir = os.path.join(self._get_sysinfodir(test.outputdir), iter_dir)
        if not os.path.exists(logdir):
            os.mkdir(logdir)
        return logdir

    @log.log_and_ignore_errors("post-reboot sysinfo error:")
    def log_per_reboot_data(self):
        """ Logging hook called whenever a job starts, and again after
        any reboot. """
        logdir = self._get_boot_subdir(next=True)
        if not os.path.exists(logdir):
            os.mkdir(logdir)

        for log in (self.test_loggables | self.boot_loggables):
            log.run(logdir)

        if _LOG_INSTALLED_PACKAGES:
            # also log any installed packages
            installed_path = os.path.join(logdir, "installed_packages")
            installed_packages = "\n".join(self.sm.list_all()) + "\n"
            utils.open_write_close(installed_path, installed_packages)

    @log.log_and_ignore_errors("pre-test sysinfo error:")
    def log_before_each_test(self, test):
        """ Logging hook called before a test starts. """
        if _LOG_INSTALLED_PACKAGES:
            self._installed_packages = self.sm.list_all()
            # Also log the list of installed packaged before each test starts
            test_sysinfodir = self._get_sysinfodir(test.outputdir)
            installed_path = os.path.join(test_sysinfodir, "installed_packages")
            installed_packages = "\n".join(self._installed_packages)
            utils.open_write_close(installed_path, installed_packages)

        if os.path.exists("/var/log/messages"):
            stat = os.stat("/var/log/messages")
            self._messages_size = stat.st_size
            self._messages_inode = stat.st_ino
        elif os.path.exists("/var/log/syslog"):
            stat = os.stat("/var/log/syslog")
            self._messages_size = stat.st_size
            self._messages_inode = stat.st_ino

    @log.log_and_ignore_errors("post-test sysinfo error:")
    def log_after_each_test(self, test):
        """ Logging hook called after a test finishs. """
        test_sysinfodir = self._get_sysinfodir(test.outputdir)

        # create a symlink in the test sysinfo dir to the current boot
        reboot_dir = self._get_boot_subdir()
        assert os.path.exists(reboot_dir)
        symlink_dest = os.path.join(test_sysinfodir, "reboot_current")
        symlink_src = utils.get_relative_path(reboot_dir,
                                              os.path.dirname(symlink_dest))
        try:
            os.symlink(symlink_src, symlink_dest)
        except Exception, e:
            raise Exception('%s: whilst linking %s to %s' % (e, symlink_src,
                                                             symlink_dest))

        # run all the standard logging commands
        for log in self.test_loggables:
            log.run(test_sysinfodir)

        # grab any new data from the system log
        self._log_messages(test_sysinfodir)

        # log some sysinfo data into the test keyval file
        keyval = self.log_test_keyvals(test_sysinfodir)
        test.write_test_keyval(keyval)

        if _LOG_INSTALLED_PACKAGES:
            # log any changes to installed packages
            old_packages = set(self._installed_packages)
            new_packages = set(self.sm.list_all())
            added_path = os.path.join(test_sysinfodir, "added_packages")
            added_packages = "\n".join(new_packages - old_packages) + "\n"
            utils.open_write_close(added_path, added_packages)
            removed_path = os.path.join(test_sysinfodir, "removed_packages")
            removed_packages = "\n".join(old_packages - new_packages) + "\n"
            utils.open_write_close(removed_path, removed_packages)

    @log.log_and_ignore_errors("pre-test siteration sysinfo error:")
    def log_before_each_iteration(self, test, iteration=None):
        """ Logging hook called before a test iteration."""
        if not iteration:
            iteration = test.iteration
        logdir = self._get_iteration_subdir(test, iteration)

        for log in self.before_iteration_loggables:
            log.run(logdir)

    @log.log_and_ignore_errors("post-test siteration sysinfo error:")
    def log_after_each_iteration(self, test, iteration=None):
        """ Logging hook called after a test iteration."""
        if not iteration:
            iteration = test.iteration
        logdir = self._get_iteration_subdir(test, iteration)

        for log in self.after_iteration_loggables:
            log.run(logdir)

    def _log_messages(self, logdir):
        """ Log all of the new data in the system log. """
        try:
            # log all of the new data in the system log
            logpaths = ["/var/log/messages", "/var/log/syslog"]
            for logpath in logpaths:
                if os.path.exists(logpath):
                    break
            else:
                raise ValueError("System log file not found (looked for %s)" %
                                 logpaths)

            bytes_to_skip = 0
            if hasattr(self, "_messages_size"):
                current_inode = os.stat(logpath).st_ino
                if current_inode == self._messages_inode:
                    bytes_to_skip = self._messages_size
            in_messages = open(logpath)
            out_file_basename = os.path.basename(logpath) + ".gz"
            out_file_name = os.path.join(logdir, out_file_basename)
            out_messages = gzip.GzipFile(out_file_name, "w")
            try:
                in_messages.seek(bytes_to_skip)
                while True:
                    # Read data in managable chunks rather than all at once.
                    in_data = in_messages.read(200000)
                    if not in_data:
                        break
                    out_messages.write(in_data)
            finally:
                out_messages.close()
                in_messages.close()
        except ValueError, e:
            logging.info(e)
        except (IOError, OSError):
            logging.info("Not logging %s (lack of permissions)", logpath)
        except Exception, e:
            logging.info("System log collection failed: %s", e)

    @staticmethod
    def _read_sysinfo_keyvals(loggables, logdir):
        keyval = {}
        for log in loggables:
            if log.log_in_keyval:
                keyval["sysinfo-" + log.logf] = log.readline(logdir)
        return keyval

    def log_test_keyvals(self, test_sysinfodir):
        """ Logging hook called by log_after_each_test to collect keyval
        entries to be written in the test keyval. """
        keyval = {}

        # grab any loggables that should be in the keyval
        keyval.update(self._read_sysinfo_keyvals(
            self.test_loggables, test_sysinfodir))
        keyval.update(self._read_sysinfo_keyvals(
            self.boot_loggables,
            os.path.join(test_sysinfodir, "reboot_current")))

        # remove hostname from uname info
        # Linux lpt36 2.6.18-smp-230.1 #1 [4069269] SMP Fri Oct 24 11:30:...
        if "sysinfo-uname" in keyval:
            kernel_vers = " ".join(keyval["sysinfo-uname"].split()[2:])
            keyval["sysinfo-uname"] = kernel_vers

        # grab the total avail memory, not used by sys tables
        path = os.path.join(test_sysinfodir, "reboot_current", "meminfo")
        if os.path.exists(path):
            mem_data = open(path).read()
            match = re.search(r"^MemTotal:\s+(\d+) kB$", mem_data,
                              re.MULTILINE)
            if match:
                keyval["sysinfo-memtotal-in-kb"] = match.group(1)

        # guess the system's total physical memory, including sys tables
        keyval["sysinfo-phys-mbytes"] = utils_memory.rounded_memtotal() // 1024

        # return what we collected
        return keyval
