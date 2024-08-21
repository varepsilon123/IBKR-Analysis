import unittest
from unittest.mock import patch, MagicMock
from src.controller.auth import (
    get_auth_status, init_brokerage_session, tickle,
    validate_sso, logout, auth_test
)

class TestAuth(unittest.TestCase):

    @patch('src.controller.auth.post')
    def test_get_auth_status(self, mock_post):
        mock_post.return_value = {'status': 'Authenticated'}
        response = get_auth_status()
        self.assertEqual(response, {'status': 'Authenticated'})
        mock_post.assert_called_once()

    @patch('src.controller.auth.post')
    def test_init_brokerage_session(self, mock_post):
        mock_post.return_value = {'session': 'initialized'}
        response = init_brokerage_session()
        self.assertEqual(response, {'session': 'initialized'})
        mock_post.assert_called_once()

    @patch('src.controller.auth.post')
    def test_tickle(self, mock_post):
        mock_post.return_value = {'message': 'Tickle successful'}
        response = tickle()
        self.assertEqual(response, {'message': 'Tickle successful'})
        mock_post.assert_called_once()

    @patch('src.controller.auth.get')
    def test_validate_sso(self, mock_get):
        mock_get.return_value = {'sso': 'valid'}
        response = validate_sso()
        self.assertEqual(response, {'sso': 'valid'})
        mock_get.assert_called_once()

    @patch('src.controller.auth.post')
    def test_logout(self, mock_post):
        mock_post.return_value = {'status': 'Logged out'}
        response = logout()
        self.assertEqual(response, {'status': 'Logged out'})
        mock_post.assert_called_once()

    @patch('src.controller.auth.get_auth_status')
    @patch('src.controller.auth.init_brokerage_session')
    @patch('src.controller.auth.tickle')
    @patch('src.controller.auth.validate_sso')
    def test_auth_test(self, mock_validate_sso, mock_tickle, mock_init, mock_get_auth):
        mock_get_auth.return_value = {'status': 'Authenticated'}
        mock_init.return_value = {'session': 'initialized'}
        mock_tickle.return_value = {'message': 'Tickle successful'}
        mock_validate_sso.return_value = {'sso': 'valid'}

        with patch('builtins.print') as mock_print:
            auth_test()

        self.assertEqual(mock_print.call_count, 4)
        mock_get_auth.assert_called_once()
        mock_init.assert_called_once()
        mock_tickle.assert_called_once()
        mock_validate_sso.assert_called_once()

if __name__ == '__main__':
    unittest.main()