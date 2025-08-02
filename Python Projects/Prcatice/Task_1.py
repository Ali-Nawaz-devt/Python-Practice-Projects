# #even odd checker
# num=int (input("Enter number : "))
# if num==0:
#     print("zero")
# elif num%2==0:
#     print("Even")
# elif num%2==1:
#     print("odd")

# Atm machine system

pin=1234

balance =2000
accoutn_owner='Ali'

Pass= int(input("Enter the password : "))
if Pass==pin:

    print('--------------------------')
    print(f'Welcome {accoutn_owner}')
    print("1.Withdraw")
    print("2.Deposit")
    print("3.Check balance : ")
    choice=int(input())
    if choice==3:
        print(f'Balance : {balance}')
    elif choice==2:
        deposit=int(input("Enter Amount :"))
        balance+=deposit
        print("Deposit Successfull")
    elif choice==1:
        withdraw_amount=int(input("Enter Amount : "))
        if withdraw_amount<=balance:
            balance-=withdraw_amount
            print(f'Withdraw Successfull : Remaining balance is {balance}')
        else:
            print("insufficent Balance ")
    else:
        print("invalid Choice ")
else:
    print("Inalid Password")
