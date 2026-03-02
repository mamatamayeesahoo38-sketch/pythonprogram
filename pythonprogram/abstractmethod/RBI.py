from abc import ABC, abstractmethod
class RBI(ABC):

    @abstractmethod
    def rate_of_interest(self):
        pass

    @abstractmethod
    def minimum_balance(self):
        pass
class SBI(RBI):

    def rate_of_interest(self):
        print("SBI Interest Rate = 6%")

    def minimum_balance(self):
        print("SBI Minimum Balance = 3000")
class PNB(RBI):

    def rate_of_interest(self):
        print("PNB Interest Rate = 6.5%")

    def minimum_balance(self):
        print("PNB Minimum Balance = 2000")


# Object Creation
s = SBI()
s.rate_of_interest()
s.minimum_balance()

p = PNB()
p.rate_of_interest()
p.minimum_balance()