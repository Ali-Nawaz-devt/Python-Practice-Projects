

conditions=input().split(" ")
k=int(conditions[0])
m=int(conditions[1])


lists=[]
for _ in range(k):
    current=input().split(" ")
    lists.append(list(map(int, current[1:])))

result=[[]
        ]
for current_list in lists:
    temp=[]
    for prefix in result:
        
        for item in current_list:
            
            temp.append(prefix+[item])
        result=temp

remainder=[]  
for number_list in result:
    addition=0
    for number in number_list:
        addition=addition+(number*number)
    remainder.append(addition % m)

remainder.sort()
print(remainder[len(remainder)-1])


