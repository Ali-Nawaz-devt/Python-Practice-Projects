Marks=[]
name=[]
i=0
toper=-1
while i<=5:
    Name=str(input("Enter Student Name : "))
    name.append(Name)
    marks=float(input("Enter Student Marks : "))
    Marks.append(marks)
    if(toper==-1):
        toper=i
    elif Marks[i]>=Marks[toper]:
        toper=i
    
    
    i+=1

print(f'The Topper Is {name[toper]}  and his Marks is {Marks[toper]}')

