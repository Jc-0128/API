import unittest
from bankaccount.bankaccount import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Alice")

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 0)

    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.balance, 100)

    def test_withdraw(self):
        self.account.deposit(100)
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)

    def test_insufficient_balance(self):
        self.account.deposit(50)
        with self.assertRaises(ValueError):
            self.account.withdraw(100)

    def test_invalid_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

if __name__ == "__main__":
    unittest.main()
