Exist_Members={'Ali','Nawaz','Ronaldo'}
name=input("Please Enter your name : ")
if Exist_Members.__contains__(name):
    print("WellCome to Club")
else:
    print("Sorry Membership Doesn't exists ")
    res=input("Do You Want To Become Member (Y?N) : ")
    if res=="Y":
        Exist_Members.add(name)
        print("Congrats You Became Member ")
    else:
        print("You Name is Not added in Membership ")