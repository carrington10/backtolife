import unittest
from bank import bank

class TestBank(unittest.TestCase):
    def test_list_account_info(self):
        account = bank("tom","09/12/2005","Seattle Washington","355678")
        expected = "This is your account info \nName:tom \nDob:09/12/2005 \nAccount Number:355678"
        self.asseertEqual(account.listaccountinfo(),expected)

if __name__ == '__main__':
    unittest.main()