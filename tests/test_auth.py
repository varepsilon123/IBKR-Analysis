import unittest
from unittest.mock import patch, MagicMock
from src.controller.auth import (
    get_auth_status, init_brokerage_session, tickle,
    validate_sso, logout, auth_test
)

class TestAuth(unittest.TestCase):

    @patch('src.controller.auth.post')
    def test_get_auth_status_success(self, mock_post):
        expected_response = {
            'authenticated': True,
            'competing': False,
            'connected': True,
            'message': '',
            'MAC': 'AA:BB:CC:DD:EE:FF',
            'serverInfo': {
                'serverName': 'MockServer123',
                'serverVersion': 'Build 9.99.9m, Jan 1, 2025 12:00:00 AM'
            },
            'hardware_info': 'mock123|AA:BB:CC:DD:EE:FF',
            'fail': ''
        }
        mock_post.return_value = expected_response
        response = get_auth_status()
        self.assertEqual(response, expected_response)
        mock_post.assert_called_once()

    @patch('src.controller.auth.post')
    def test_get_auth_status_failure(self, mock_post):
        mock_post.return_value = {'authenticated': False, 'fail': 'Connection error'}
        response = get_auth_status()
        self.assertFalse(response['authenticated'])
        self.assertEqual(response['fail'], 'Connection error')
        mock_post.assert_called_once()

    @patch('src.controller.auth.post')
    def test_init_brokerage_session_success(self, mock_post):
        expected_response = {
            'authenticated': True,
            'competing': False,
            'connected': True,
            'message': '',
            'MAC': 'AA:BB:CC:DD:EE:FF',
            'serverInfo': {
                'serverName': 'MockServer123',
                'serverVersion': 'Build 9.99.9m, Jan 1, 2025 12:00:00 AM'
            },
            'hardware_info': 'mock123|AA:BB:CC:DD:EE:FF'
        }
        mock_post.return_value = expected_response
        response = init_brokerage_session()
        self.assertEqual(response, expected_response)
        mock_post.assert_called_once()

    @patch('src.controller.auth.post')
    def test_init_brokerage_session_failure(self, mock_post):
        mock_post.return_value = {'authenticated': False, 'message': 'Invalid credentials'}
        response = init_brokerage_session()
        self.assertFalse(response['authenticated'])
        self.assertEqual(response['message'], 'Invalid credentials')
        mock_post.assert_called_once()

    @patch('src.controller.auth.post')
    def test_tickle_success(self, mock_post):
        expected_response = {
            'session': 'abcdef1234567890abcdef1234567890',
            'ssoExpires': 300000,
            'collission': False,
            'userId': 12345678,
            'hmds': {'error': 'no bridge'},
            'iserver': {
                'authStatus': {
                    'authenticated': True,
                    'competing': False,
                    'connected': True,
                    'message': '',
                    'MAC': 'AA:BB:CC:DD:EE:FF',
                    'serverInfo': {
                        'serverName': 'MockServer123',
                        'serverVersion': 'Build 9.99.9m, Jan 1, 2025 12:00:00 AM'
                    },
                    'hardware_info': 'mock123|AA:BB:CC:DD:EE:FF'
                }
            }
        }
        mock_post.return_value = expected_response
        response = tickle()
        self.assertEqual(response, expected_response)
        mock_post.assert_called_once()

    @patch('src.controller.auth.post')
    def test_tickle_failure(self, mock_post):
        mock_post.return_value = {'session': None, 'error': 'Session expired'}
        response = tickle()
        self.assertIsNone(response['session'])
        self.assertEqual(response['error'], 'Session expired')
        mock_post.assert_called_once()

    @patch('src.controller.auth.get')
    def test_validate_sso_success(self, mock_get):
        expected_response = {
            'USER_ID': 12345678,
            'USER_NAME': 'mockuser123',
            'RESULT': True,
            'AUTH_TIME': 1609459200000,
            'SF_ENABLED': True,
            'IS_FREE_TRIAL': False,
            'CREDENTIAL': 'mockuser123',
            'IP': '192.168.1.100',
            'EXPIRES': 300000,
            'QUALIFIED_FOR_MOBILE_AUTH': None,
            'LANDING_APP': 'PORTAL',
            'IS_MASTER': False,
            'lastAccessed': 1609462800000,
            'features': {
                'env': 'TEST',
                'wlms': True,
                'realtime': True,
                'bond': True,
                'optionChains': True,
                'calendar': True,
                'newMf': True
            },
            'region': 'US'
        }
        mock_get.return_value = expected_response
        response = validate_sso()
        self.assertEqual(response, expected_response)
        mock_get.assert_called_once()

    @patch('src.controller.auth.get')
    def test_validate_sso_failure(self, mock_get):
        mock_get.return_value = {'RESULT': False, 'ERROR': 'Invalid SSO token'}
        response = validate_sso()
        self.assertFalse(response['RESULT'])
        self.assertEqual(response['ERROR'], 'Invalid SSO token')
        mock_get.assert_called_once()

    @patch('src.controller.auth.post')
    def test_logout_success(self, mock_post):
        mock_post.return_value = {'status': True}
        response = logout()
        self.assertEqual(response, {'status': True})
        mock_post.assert_called_once()

    @patch('src.controller.auth.post')
    def test_logout_failure(self, mock_post):
        mock_post.return_value = {'status': False, 'error': 'Logout failed'}
        response = logout()
        self.assertFalse(response['status'])
        self.assertEqual(response['error'], 'Logout failed')
        mock_post.assert_called_once()

    @patch('src.controller.auth.post')
    def test_network_error(self, mock_post):
        mock_post.side_effect = Exception("Network error")
        with self.assertRaises(Exception):
            get_auth_status()

    @patch('src.controller.auth.get_auth_status')
    def test_auth_test_success(self, mock_get_auth_status):
        mock_get_auth_status.return_value = {'authenticated': True}
        with patch('builtins.print') as mock_print:
            auth_test()
            mock_print.assert_called_with("Response Body: {'authenticated': True}")

    @patch('src.controller.auth.get_auth_status')
    def test_auth_test_exception(self, mock_get_auth_status):
        mock_get_auth_status.side_effect = Exception("Test exception")
        with patch('builtins.print') as mock_print:
            auth_test()
            mock_print.assert_called_with("Error: Test exception")

if __name__ == '__main__':
    unittest.main()