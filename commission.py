class Commission:
    def __init__(self, commission):
        self.commission = commission
    
    def getCommission(self):
        return self.commission

    def __str__(self):
        return None

class FixedBonus(Commission):
    def __init__(self, bonus):
        super().__init__(bonus)

    def __str__(self):
        return 'bonus commission of ' + str(self.commission) + '.'

class NumContracts(Commission):
    def __init__(self, commission_per_contract, numContracts):
        self.numContracts = numContracts
        self.commission_per_contract = commission_per_contract
        commission = numContracts * commission_per_contract
        super().__init__(commission)

    def __str__(self):
        return 'commission for ' + str(self.numContracts) + ' contract(s) at ' + str(self.commission_per_contract) + '/contract.'