from abc import ABC, abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def calculate_interest(self):
        pass


class SavingAccount(BankAccount):

    def calculate_interest(self):
        print("Saving Account Interest = 5%")


class CurrentAccount(BankAccount):

    def calculate_interest(self):
        print("Current Account Interest = 2%")


s = SavingAccount()
s.calculate_interest()
