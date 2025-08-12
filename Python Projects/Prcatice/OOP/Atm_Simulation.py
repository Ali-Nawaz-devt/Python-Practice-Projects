class Account:
    def __init__(self, account_number, account_holder, balance=0, Account_pass=None):
        """Initialize the account with account number, holder, balance, and password."""
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.Account_pass = Account_pass


class Bank:
    def __init__(self):
        """Initialize the bank with an empty list of accounts."""
        self.accounts = []

    def create_account(self, account_number, account_holder, initial_balance=0, Account_pass=None):
        """Create a new account and add it to the bank."""
        new_account = Account(account_number, account_holder, initial_balance, Account_pass)
        self.accounts.append(new_account)
        print(f"Account created for {account_holder} with account number {account_number}.")

    def authenticate_account(self, account_number, Account_pass):
        """Authenticate an account using account number and password."""
        for account in self.accounts:
            if account.account_number == account_number and account.Account_pass == Account_pass:
                print(f"Authentication successful for account number {account_number}.")
                return account
        print(f"Authentication failed for account number {account_number}.")
        return None
    
class AtmSimulation:
    def __init__(self,Bank):
        """Initialize the ATM simulation with a bank instance."""
        self.bank = Bank
    def Withdraw(self, account, amount):
        """Withdraw an amount from the account if sufficient balance exists."""
        for account_  in self.bank.accounts:
            if account_.Account_pass == account.Account_pass:
                if amount > 0 and amount <= account.balance:
                    account.balance -= amount
                    print(f"Withdraw Complete. New Balance: {account.balance}")
                    account_=account
                else:
                    print("Invalid Amount")
            
    def Deposit(self, account, amount):
        """Deposit an amount into the account."""
        for account_  in self.bank.accounts:
            if account_.Account_pass == account.Account_pass:
                if amount > 0:
                    account.balance += amount
                    print(f"Deposit Complete. New Balance: {account.balance}")
                    account_=account
                else:
                    print("Invalid Amount")
           
           
    def Check_Balance(self, account):
        """Check the balance of the account."""
        for account_ in self.bank.accounts:
            if account.Account_pass ==account.Account_pass:
                print(f"Balance: {account.balance}")
            else:
                print("Incorrect Password")
       
       


# Example usage
Bank=Bank()
while True:
    
    print("1. Bank ")
    print("2. ATM Simulation")
    print("3. Exit")    
    choice=int(input())
    if choice==1:
        while True:

            print("------WellCome to Bank-----------")
            print("1. Account Creation")
            print("2.Account Authentication")
            print("3. Exist")
            ch=int(input())

            if ch ==1 :
                account_holder=input("Please Enter your Name : ")
                account_number=int(input("Please Enter Account Number : "))
                account_balance=float(input("Please Enter Amount You Want To deposit : "))
                account_pass=int(input("Please Enter Account Password : "))
                Bank.create_account(account_number,account_holder,account_balance,account_pass)
            if ch==2:
                account_number=int(input("Please Enter Account Number : "))
                account_pass=int(input("Please Enter Account Password : "))
                Bank.authenticate_account(account_number,account_pass)
            if ch==3:
                break
    if choice==2:
        Atm=AtmSimulation(Bank)
        
        
        
        
        account_number=int(input("Please Enter Account Number : "))
        account_pass=int(input("Please Enter Account Password : "))
            
        Account=Bank.authenticate_account(account_number,account_pass)
        if Account!=None:
            while True:


                print("1. Withdraw")
                print("2. Deposit")
                print("3. Balance")
                print("4. Exist")
                ch=int(input())
                if ch==1:
                    Amount=float(input("Enter Amount :"))
                    Atm.Withdraw(Account,Amount)
                if ch==2:
                    Amount=float(input("Enter Amount :"))
                    Atm.Deposit(Account,Amount)
                if ch==3:
                    Atm.Check_Balance(Account)
                if ch==4:
                    break

    if choice==3:
        break
    



        









