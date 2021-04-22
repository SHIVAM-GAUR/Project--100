class Atm(object):
    def __init__(self, AtmCardNumber, pinNumber):
        self.AtmCardNumber = AtmCardNumber
        self.pinNumber = pinNumber
        

    def CashWithdrawal(self):
        print("Cash Withdrawal called")

    def BalanceEnquiry(self):
        print("Balance Enquiry Called" )


# Define some students
john = Atm(123,123)
jane = Atm(76855,2367884)

# Now we can get to the grades easily
john.CashWithdrawal()
jane.BalanceEnquiry()