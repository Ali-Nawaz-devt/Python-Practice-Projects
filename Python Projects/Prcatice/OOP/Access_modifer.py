class Person:
    
    def __init__(self,name,pass_):
        self.name=name
        self.__pass=pass_
    def Private(self):
        return self.__pass

person=Person("ali",123)

print(f"Public Attribute : {person.name}")
print(f"Private Attribute : {person.Private()}")

    
        
        
