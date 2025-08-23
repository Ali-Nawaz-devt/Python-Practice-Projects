Points=[(4,11),(7,13),
        (9,10),(12,12),
        (14,10),(15,7),
        (7,7),(11,5),
        (13,3),(2,5),
        (4,4),(5,1),
        ]

Maximal=[]

for Point_1 in Points:
    is_Maximal=True
    for Point_2 in Points:
        if Point_2!=Point_1 and (Point_1[0]<=Point_2[0] and Point_1[1]<=Point_2[1] ):
            is_Maximal=False
            break

    if is_Maximal:
        Maximal.append(Point_1)
    

print(Maximal)
        
