def Sum_natural(n):
    if(n==0):
        return 0
    return Sum_natural(n-1) + n 
print(Sum_natural(10))