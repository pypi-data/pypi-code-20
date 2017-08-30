from unittest.case import TestCase

from tweepy.error import TweepError

from responsebot.common.exceptions import MissingConfigError, APIQuotaError, AuthenticationError

try:
    from mock import patch, MagicMock
except ImportError:
    from unittest.mock import patch, MagicMock

from responsebot.responsebot import ResponseBot


class ResponseBotTestCase(TestCase):
    def test_call_necessary_utils(self):
        handler_classes = [MagicMock]
        client = MagicMock()
        listener = MagicMock()

        with patch('responsebot.utils.handler_utils.discover_handler_classes', return_value=handler_classes) \
                as mock_discover, \
                patch('responsebot.utils.auth_utils.auth', return_value=client) as mock_auth, \
                patch('responsebot.responsebot.ResponseBotListener', return_value=listener) as mock_listener, \
                patch('responsebot.responsebot.ResponseBotStream') as mock_stream:
            ResponseBot(
                handlers_package='some_package',
                auth=('ck', 'cs', 'tk', 'ts'),
            ).start()

            self.assertTrue(mock_auth.called)
            self.assertTrue(mock_discover.called)
            mock_listener.assert_called_once_with(client=client, handler_classes=handler_classes)
            mock_stream.assert_called_once_with(client=client, listener=listener)
            mock_stream().start.assert_called_once_with()

    @patch('logging.error')
    def test_log_missing_config_exception(self, mock_log):
        exception = MissingConfigError('message')

        with patch('responsebot.responsebot.ResponseBotConfig', side_effect=exception):
            self.assertRaises(SystemExit, ResponseBot)
            mock_log.assert_called_once_with('message')

    @patch('logging.warning')
    def test_log_no_handler_classes_warning(self, mock_log):
        with patch('responsebot.responsebot.ResponseBotConfig'),\
                patch('responsebot.utils.handler_utils.discover_handler_classes', return_value=[]),\
                patch('responsebot.utils.auth_utils.auth'),\
                patch('responsebot.responsebot.ResponseBotStream'):
            ResponseBot().start()
            mock_log.assert_called_once_with('No handler found. Did you forget to extend BaseTweethandler?'
                                             ' Check --handlers-module')

    @patch('logging.exception')
    def test_log_auth_error(self, mock_log):
        for exception in [APIQuotaError('message'), AuthenticationError('message')]:
            mock_log.reset_mock()
            with patch('responsebot.responsebot.ResponseBotConfig', return_value={
                'min_seconds_between_errors': 30, 'sleep_seconds_on_consecutive_errors': 300
                }),\
                    patch('responsebot.utils.handler_utils.discover_handler_classes', return_value=[MagicMock]),\
                    patch('responsebot.utils.auth_utils.auth', side_effect=exception),\
                    patch('responsebot.responsebot.time.sleep'):
                self.assertRaises(SystemExit, ResponseBot().start)
                mock_log.assert_called_with('try to sleep if there are repeating errors.')

    @patch('logging.exception')
    def test_log_stream_api_error(self, mock_log):
        exception = TweepError('message')
        with patch('responsebot.responsebot.ResponseBotConfig', return_value={
                'min_seconds_between_errors': 30, 'sleep_seconds_on_consecutive_errors': 300
                }),\
                patch('responsebot.utils.handler_utils.discover_handler_classes', return_value=[MagicMock]),\
                patch('responsebot.utils.auth_utils.auth'),\
                patch('responsebot.responsebot.ResponseBotListener'),\
                patch('responsebot.responsebot.ResponseBotStream', side_effect=exception),\
                patch('responsebot.responsebot.time.sleep'):
            self.assertRaises(SystemExit, ResponseBot().start)
            mock_log.assert_called_with('try to sleep if there are repeating errors.')
