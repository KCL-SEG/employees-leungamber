"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
from commission import *
from contract import *

class Employee:
    def __init__(self, name, contract: Contract, commission: Commission = None):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        if self.commission is not None:
            return self.contract.getContract() + self.commission.getCommission()
        else:
            return self.contract.getContract()

    def __str__(self):
        if self.commission is None:
            return self.name + " works on a " +  str(self.contract) + '. Their total pay is ' + str(self.get_pay()) + '.'
        else:
            return self.name + " works on a " +  str(self.contract) + ' and receives a ' + str(self.commission) + ' Their total pay is ' + str(self.get_pay()) + '.'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', SalaryContract(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyContract(25, 100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', SalaryContract(3000), NumContracts(200, 4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyContract(25, 150), NumContracts(220, 3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', SalaryContract(2000), FixedBonus(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyContract(30, 120), FixedBonus(600))
