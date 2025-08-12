
class human:
    name=None


class Employee(human):
    
    def __init__(self,name):
        super().name=name
    
    def info(self):
        print(self.name)
        

Employee=Employee("Ali")
Employee.info()




    