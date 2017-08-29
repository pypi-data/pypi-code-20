# -*- coding: utf-8 -*-

import inspect
import logging
import logging.handlers
import os
import re
import sys
from contextlib import contextmanager
from datetime import datetime

from lore import ansi, env

if sys.version_info.major == 3:
    import shutil


class SecretFilter(logging.Filter):
    PASSWORD_MATCH = re.compile(
        r'((secret|key|access|pass|pw).*?[=:][^\w]*)\w+',
        flags=re.IGNORECASE
    )
    URL_MATCH = re.compile(
        r'://([^:]+):([^@]+)(@.+)',
        flags=re.IGNORECASE
    )
    
    def filter(self, record):
        if record is None:
            return True
        record.msg = str(record.msg)
        record.msg = re.sub(SecretFilter.PASSWORD_MATCH, r'\1XXX', record.msg)
        record.msg = re.sub(SecretFilter.URL_MATCH, r'://XXX:XXX\3', record.msg)
        return True


class ConsoleFormatter(logging.Formatter):
    colors = {
        logging.DEBUG: ansi.debug,
        logging.INFO: ansi.info,
        logging.WARNING: ansi.warning,
        logging.ERROR: ansi.error,
        logging.CRITICAL: ansi.critical
    }
    
    def format(self, record):
        timestamp = datetime.fromtimestamp(record.created).strftime('%H:%M:%S')
        timestamp = timestamp + '.%03d' % record.msecs
        level = '%-8s' % record.levelname
        level = ConsoleFormatter.colors[record.levelno](level)
        location = ansi.foreground(ansi.CYAN, record.name) + ':' + \
                   ansi.foreground(ansi.CYAN, str(record.lineno))

        return '%s  %s %s => %s' % (timestamp, level, location, record.msg)


logger = logging.getLogger()

def add_log_file_handler(path):
    if not os.path.exists(os.path.dirname(path)):
        os.mkdir(os.path.dirname(path))
    handler = logging.FileHandler(path)
    handler.setFormatter(ConsoleFormatter())
    handler.addFilter(SecretFilter())
    logger.addHandler(handler)

def add_log_stream_handler(stream=sys.stdout):
    handler = logging.StreamHandler(stream)
    handler.setFormatter(ConsoleFormatter())
    handler.addFilter(SecretFilter())
    logger.addHandler(handler)

def add_syslog_handler(address):
    syslog = logging.handlers.SysLogHandler(address=address)
    syslog.setFormatter(logging.Formatter(fmt='%(name)s:%(lineno)s %(message)s'))
    syslog.addFilter(SecretFilter())
    logger.addHandler(syslog)

if env.exists():
    logfile = os.path.join(env.log_dir, env.name + '.log')
    add_log_file_handler(logfile)
    
try:
    if env.name == env.DEVELOPMENT and os.getpgrp() == os.tcgetpgrp(sys.stdout.fileno()):
        # running in a terminal foreground
        add_log_stream_handler()
    else:
        # running in a terminal background
        pass
except OSError:
    # not running in a terminal
    pass

log_levels = {
    env.DEVELOPMENT: logging.DEBUG,
    env.TEST: logging.DEBUG,
}
logger.setLevel(log_levels.get(env.name, logging.INFO))


if env.name != env.DEVELOPMENT and env.name != env.TEST:
    address = None
    for f in ('/dev/log', '/var/run/syslog',):
        if os.path.exists(f):
            address = f
            break
            
    if address:
        add_syslog_handler(address)


def strip_one_off_handlers():
    global logger
    for child in logging.Logger.manager.loggerDict.values():
        if isinstance(child, logging.Logger):
            for one_off in child.handlers:
                child.removeHandler(one_off)
            child.setLevel(logger.level)

strip_one_off_handlers()


@contextmanager
def timer(message="elapsed time:", level=logging.INFO):
    start = datetime.now()
    try:
        yield
    finally:
        calling_logger(3).log(level, '%s %s' % (message, datetime.now() - start))


def which(command):
    if sys.version_info.major < 3:
        paths = os.environ['PATH'].split(os.pathsep)
        return any(
            os.access(os.path.join(path, command), os.X_OK) for path in paths
        )
    else:
        return shutil.which(command)


def calling_logger(height=1):
    """ Obtain a logger for the calling module.

    Uses the inspect module to find the name of the calling function and its
    position in the module hierarchy. With the optional height argument, logs
    for caller's caller, and so forth.
    
    see: http://stackoverflow.com/a/900404/48251
    """
    caller = inspect.stack()[height]
    scope = caller[0].f_globals
    path = scope['__name__']
    if path == '__main__':
        path = scope['__package__'] or os.path.basename(sys.argv[0])
    return logging.getLogger(path)
