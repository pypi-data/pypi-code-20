# coding: utf-8
""" Rabbit and pika wrapper, to have just what we nee and not deal with all
config stuff every time a message is send. The envelope used for this version will be created as
follows specified in the message documentation. A sender is also written with te same purpose

"""

import logging
import pika
from ..basemsg import BasicMessage
from deployv.helpers import configuration


_logger = logging.getLogger(__name__)


class BaseRabbitConfiguration(object):
    """ As the configuration for the sender can be from various sources this will be the base
    class for that, so there is no need to rewrite or change any code from the sender.
    Just need to be sure thar the parameters are fully filled

    :param host: Hostname or ip where the rabbitmq server is hosted
    :param user: Username to login
    :param password: User password
    :param virtual_host: rabbitmq virtual host
    :param queue: The queue prefix to use, the complete name is generated using queue+node_id
    :param exchange: Message exchange to use (mus be the same for all nodes or group)
    :param route: route name where the message will be send ie: test.task.node_id to send
                    a message to all nodes just use test.task
    :param timeout: Connection timeout in seconds
    """
    def __init__(self,
                 host,
                 port,
                 user,
                 password,
                 virtual_host,
                 queue,
                 exchange,
                 route,
                 result=False,
                 timeout=5.0,
                 ssl=True):
        self.result_config = result
        self.user = user
        self.password = password
        self.credentials = pika.PlainCredentials(self.user, self.password)
        self.parameters = pika.ConnectionParameters(
            host=host,
            port=int(port),
            virtual_host=virtual_host,
            credentials=self.credentials,
            ssl=ssl)
        self.parameters.socket_timeout = timeout
        self.queue_name = queue
        self.exchange_name = exchange
        self.route = route
        self.properties = pika.BasicProperties(content_type='application/json',
                                               delivery_mode=2)


class FileRabbitConfiguration(BaseRabbitConfiguration):
    """Reads the configuration from a ini-style file and builds the base
    configuration.

    :param config_object: DeployvConfig instance that contains the configuration read from
        the config files
    :param result: If you need the result configuration or not, this is in the case the workers
        are going to send and ack, result or status message
    """
    def __init__(self, config_object, result=False):
        if isinstance(config_object, (configuration.DeployvConfig, BasicMessage)):
            self.config = config_object.config
        else:
            raise ValueError('No valid config object provided')
        self._config_object = config_object
        user = self.config.get('rmq', 'rmq_user')
        passwd = self.config.get('rmq', 'rmq_passwd')
        host = self.config.get('rmq', 'rmq_server')
        port = int(self.config.get('rmq', 'rmq_port'))
        vhost = self.config.get('rmq', 'rmq_vhost')
        timeout = float(self.config.get('rmq', 'rmq_timeout'))
        exchange = self.config.get('rmq', 'rmq_exchange')
        ssl = self.config.getboolean('rmq', 'rmq_ssl')
        if result:
            queue = self.config.get('rmq', 'rmq_stat_queue')
            route = self.config.get('rmq', 'rmq_stat_topic')
        else:
            queue = self.config.get('rmq', 'rmq_task_queue')
            route = self.config.get('rmq', 'rmq_task_topic')

        super(FileRabbitConfiguration, self).__init__(host, port, user, passwd, vhost, queue,
                                                      exchange, route, result, timeout, ssl)

    def get_result_object(self):
        return FileRabbitConfiguration(self._config_object, result=True)
