import unittest
from unittest.mock import patch
from src.controller.accounts import account_pnl, accounts_test, portfolio_accounts, BASE_URL

class TestAccounts(unittest.TestCase):

    @patch('src.controller.accounts.get')
    def test_account_pnl(self, mock_get):
        mock_get.return_value = {'pnl': 1000}
        response = account_pnl()
        self.assertEqual(response, {'pnl': 1000})
        mock_get.assert_called_once()

    @patch('src.controller.accounts.portfolio_accounts')
    def test_accounts_test(self, mock_portfolio_accounts):
        mock_portfolio_accounts.return_value = {'accounts': [{'id': 'test'}]}
        
        with patch('builtins.print') as mock_print:
            accounts_test()
            mock_print.assert_called_with("Response Body: {'accounts': [{'id': 'test'}]}")

        mock_portfolio_accounts.assert_called_once()

    @patch('src.controller.accounts.portfolio_accounts')
    def test_accounts_test_exception(self, mock_portfolio_accounts):
        mock_portfolio_accounts.side_effect = Exception("Test exception")
        
        with patch('builtins.print') as mock_print:
            accounts_test()
            mock_print.assert_called_with("Error: Test exception")

        mock_portfolio_accounts.assert_called_once()

    @patch('src.controller.accounts.get')
    def test_portfolio_accounts(self, mock_get):
        mock_response = {
            'accounts': [
                {'id': 'DU1234567', 'accountAlias': 'Test Account 1'},
                {'id': 'DU7654321', 'accountAlias': 'Test Account 2'}
            ]
        }
        mock_get.return_value = mock_response
        
        response = portfolio_accounts()
        
        self.assertEqual(response, mock_response)
        self.assertEqual(len(response['accounts']), 2)
        self.assertEqual(response['accounts'][0]['id'], 'DU1234567')
        self.assertEqual(response['accounts'][1]['accountAlias'], 'Test Account 2')
        
        mock_get.assert_called_once()
        mock_get.assert_called_with(url=f"{BASE_URL}/portfolio/accounts")

if __name__ == '__main__':
    unittest.main()