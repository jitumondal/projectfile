




from abc import abstractmethod


class catch:
    def __init__(self,fastname,lastname) -> None:
        self.fname = fastname
        self.lname = lastname

    @property
    def email(self):
        return f"Your email is: {self.fname}.{self.lname}@gamil.com"

    @email.setter
    def email(self,string):
        name = string.split("@")[0]
        self.fname,self.lname = name.split(".") [0],name.split(".")[1]
        
    @email.deleter  
    def email(self):
        self.fname = None  
        self.lname = None  

emp1 = catch("jitesh","mondal")

emp1.email = "jitesh.mondal@gamil.com"
print(emp1.email  )

del emp1.email
print(emp1.email)










