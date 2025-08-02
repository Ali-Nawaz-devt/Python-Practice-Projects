Tasks=[]
Completed=[]

while True:
    print("1.Add task")
    print("2.Remove")
    print("3.View Task")
    print("4.Mark Completed ")
    print("5.Exist")
    ch=int(input("Enter Choice : "))
    if ch==1:
        Tasks.append(input("Enter Task : ").capitalize)
        print("Task Added Sucessfully ")
        Completed.append(False)
    elif ch==2:
        print("Which Task you wanted to Remove ")
        print("-----------------------------------")
        print("Tasks ---------------------Completed ") 
        for i in  range(len(Tasks)):
            print(Tasks[i],'             ', Completed[i]  )
        task=input("Enter task you wanted to remove : ")
        if Tasks.remove(task.capitalize):
            print("Task Removed Suceesfully ")
        else:
            print("Task Does not Exist ")
    elif ch==5:
        break
    elif ch==3:
        print("Tasks ---------------------Completed ") 
        for i in  range(len(Tasks)):
            print(Tasks[i]+'                       ', Completed[i]  )
    elif ch==4:
        print("Tasks ---------------------Completed ") 
        for i in  range(len(Tasks)):
            print(i+1,"."+Tasks[i]+'             ', Completed[i]  )
        completed=int(input("Enter Number of Task To Mark Completed : "))
        Completed[i]=True
        print("Task Marked Completed ")
    

