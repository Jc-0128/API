import logging

class BankAccount:
    def __init__(self, account_holder: str):
        self._account_holder: str = account_holder
        self._balance: int = 0
        logging.basicConfig(level=logging.INFO)

    @property
    def account_holder(self) -> str:
        return self._account_holder

    @account_holder.setter
    def account_holder(self, user: str) -> None:
        self._account_holder = user

    @property
    def balance(self) -> int:
        return self._balance

    @balance.setter
    def balance(self, value: int) -> None:
        if value < 0:
            raise ValueError("餘額不能為負數")
        self._balance = value

    def display_balance(self) -> None:
        logging.info(f"目前餘額: {self.balance}")

    def deposit(self, amount: int) -> None:
        """ 存款方法 """
        try:
            if amount > 0:
                self.balance += amount
                self.display_balance()
            else:
                raise ValueError("無效的存款金額")
        except ValueError as e:
            logging.error(e)
            raise

    def withdraw(self, amount: int) -> None:
        """ 取款方法 """
        try:
            if self.balance >= amount:
                self.balance -= amount
                self.display_balance()
            else:
                raise ValueError("餘額不足")
        except ValueError as e:
            logging.error(e)
            raise
