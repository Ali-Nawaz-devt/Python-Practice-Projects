class bank:
    def __init__(self,initail_balance):
        self.Balance=initail_balance

    def Deposit(self,Amount):
        if Amount>0:
            self.Balance+=Amount
            print("Deposit Complete")
        else:
            print('Invalid Amount')
  
    def Withdraw(self,Amount):
        if Amount>0 and Amount<=self.Balance:
            self.Balance=self.Balance-Amount
            print("Withdraw Complete")
        else:
            print("Inavlid Amount")

    def Check_Balance(self):
        print("Balance {}: ".format(self.Balance)) 


Account_1=bank(10000)
Account_1.Check_Balance()
Account_1.Withdraw(10000)
Account_1.Deposit(1000)
Account_1.Check_Balance()

        