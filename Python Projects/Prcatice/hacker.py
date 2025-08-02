import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    count={}
    characters=[]
    same=[]
    
    for i in s:
        if s.count(i)>1 and i not in same:
            count[i]=s.count(i)
            characters.append(s.count(i))
            same.append(i)

    Multi=[]
    
    for i in same:
        Multi=[]
        if characters.count(count[i])>1:

            for u in same:
                if i!=u and count[i]==count[u]:
                    Multi.append(u)
            Multi.append(i)
            if len(Multi)>1:
                Multi.sort()
                for n in Multi:
                    print(n,count[n])
                    same.remove(n)
            

        else:


            print(i,count[i])

        



   

