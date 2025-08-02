# Enter your code here. Read input from STDIN. Print output to STDOUT
def Generate_combinations(lists_,index=0,current=[],result=[]) :
    if index==len(lists_):
        print(current)
        result.append(current[:])
        return
    for item in lists_[index]:
        current.append(item)
        
        Generate_combinations(lists_,index+1,current,result)
        current.pop()
    return result


    
  
    
lists_=Generate_combinations([
    [1,2],
    [3,4],
    [5,6]
]
)
