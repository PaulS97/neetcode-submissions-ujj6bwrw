class Account:
    def __init__(self, title: str, balance: int):
        self.title = title
        self._balance = balance
    
    def display_balance(self) -> None:
        print("Balance: $", self._balance, sep="")


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
