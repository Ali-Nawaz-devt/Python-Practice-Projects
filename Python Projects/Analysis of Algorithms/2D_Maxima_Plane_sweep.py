Points=[(4,11),(7,13),
        (9,10),(12,12),
        (14,10),(15,7),
        (7,7),(11,5),
        (13,3),(2,5),
        (4,4),(5,1),
        ]

for i in range(len(Points)):
    for j in range(len(Points)):
        if Points[i][0]<Points[j][0]:
            temp=Points[i]
            Points[i]=Points[j]
            Points[j]=temp


Stack=[]

for Point in Points:
    while len(Stack)!=0 and Point[1]>=Stack[len(Stack)-1][1]:
        Stack.pop()

    Stack.append(Point)


print(Stack)
