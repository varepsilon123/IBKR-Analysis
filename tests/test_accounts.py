import unittest
from unittest.mock import patch
from src.controller.accounts import account_pnl, accounts_test

class TestAccounts(unittest.TestCase):

    @patch('src.controller.accounts.get')
    def test_account_pnl(self, mock_get):
        mock_get.return_value = {'pnl': 1000}
        response = account_pnl()
        self.assertEqual(response, {'pnl': 1000})
        mock_get.assert_called_once()

    @patch('src.controller.accounts.account_pnl')
    def test_accounts_test(self, mock_account_pnl):
        mock_account_pnl.return_value = {'pnl': 1000}
        
        # Capture print output
        with patch('builtins.print') as mock_print:
            accounts_test()
            mock_print.assert_called_with("Response Body: {'pnl': 1000}")

        mock_account_pnl.assert_called_once()

    @patch('src.controller.accounts.account_pnl')
    def test_accounts_test_exception(self, mock_account_pnl):
        mock_account_pnl.side_effect = Exception("Test exception")
        
        # Capture print output
        with patch('builtins.print') as mock_print:
            accounts_test()
            mock_print.assert_called_with("Error: Test exception")

        mock_account_pnl.assert_called_once()

if __name__ == '__main__':
    unittest.main()
