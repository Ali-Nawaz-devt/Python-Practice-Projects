print("Welcome to Ticket Counter ")
age = int(input('Please Enter your age : '))
if age >=0 and age <=12:
    print("Tickets for Chidren is free :  ")
elif age>12 and age<=17:
    print("We provide 15% Discount For Teens")
else:
    print("Adults have to pay Full Price ")