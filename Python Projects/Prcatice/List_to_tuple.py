def merge_the_tools(string, k):
    

    list_=list(string)
    count=0
    str=''
    sub=[]
    length=len(list_)
    for i in list_:
        length-=1
        if count<k:
            if length==1:
                
                
                
                str+=i
                sub.append(str)
            else:
                
             
            
            
                count+=1
                str+=i
        else:
            count=0
            
            sub.append(str)
            str=i
    for i in sub:
        
        str=list(i)
        
        
        seen=''
        print(str)
        for n in str:
            if n not in seen:
                seen+=n
            
        print(seen)
                
                
            
               
        
          
    
    
merge_the_tools("AABCAAADA"
,3)