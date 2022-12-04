class Contract(object):

    def __init__(self, salary):
        self.salary = salary

    def getContract(self):
        return self.salary

    def __str__(self):
        return None

class SalaryContract(Contract):

    def __init__(self, salary):
        super().__init__(salary)

    def __str__(self):
        return 'monthly salary of ' + str(self.salary)


class HourlyContract(Contract):

    def __init__(self, hourly_wage, numHours):
        self.hourly_wage = hourly_wage
        self.numHours = numHours
        salary = hourly_wage * numHours
        super().__init__(salary)

    def __str__(self):
        return 'contract of ' + str(self.numHours) + ' hours at ' + str(self.hourly_wage) + '/hour'
