class Employee:
    raiseAmount=1.05
    numemp=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        Employee.numemp+=1
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    @fullname.setter
    def fullname(self,name):
        first,last=name.split(" ")
        self.first=first
        self.last=last
    @fullname.deleter
    def fullname(self):
        print("name deleted :(")
        self.first=None
        self.last=None
    @property
    def email(self):
        return f"{self.first.lower()}{self.last.lower()}@company.com"
    def applyR(self):
        self.pay*=self.raiseAmount
    @classmethod
    def set_raise(cls,amount):
        cls.raiseAmount=amount
    @classmethod
    def form_string(cls,emp):
        first,last,pay=emp.split("-")
        return cls(first,last,pay)
    @staticmethod
    def workingD(day):
        import datetime
        if day.weekday==5 or day.weekday==6:
            return False
        else:
            return True
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first,self.last,self.pay)
    def __str__(self):
        return f"{self.fullname} --> {self.email}"
    def __add__(self,other):
        return self.pay+other.pay
    def __len__(self):
        return len(self.fullname)

class Developer(Employee):
    raiseAmount=1.1
    def __init__(self,first,last,pay,lan):
        super().__init__(first,last,pay)
        self.lan=lan

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def nameP(self):
        for emp in self.employees:
            print(emp.fullname)


emp1=Employee("Ahammad","Shawki",90000)
emp2=Employee("Cristiano","Ronaldo",100000000)
dev1=Developer("Corey","Scafer",9999,"python")
man1=Manager("Zinedin","Zidan",66764,[emp2,emp1])

print(Employee.numemp)
print(Employee.raiseAmount)
Employee.set_raise(1.88)
print(Employee.raiseAmount)
print(dev1.email)

emp_str_3 ="john-doe-700"
emp_str_4 ="steve-smith-800"
emp_str_5 ="sergio-ramos-900"

emp3=Employee.form_string(emp_str_3)
print(emp3.fullname)

import datetime
my_date=datetime.datetime.strptime("2016,7,10","%Y,%m,%d").date()
print(my_date)
print(Employee.workingD(my_date))
print(dev1.pay)
dev1.applyR()
print(dev1.pay)
print(dev1.raiseAmount)
print(dev1.lan)
man1.nameP()
man1.add_emp(dev1)
man1.nameP()
man1.remove_emp(emp2)
man1.nameP()

print(isinstance(emp3,Employee))
print(isinstance(emp1,Manager))
print(issubclass(Developer,Employee))

print(emp1)
print(repr(emp1))
print(emp1.__repr__())
print(str(emp1))
print(emp1.__str__())
print(emp1+emp2)
print(emp1.__add__(emp2))
print(len(emp1))
print(emp1.__len__())


print(1+2)
print(int.__add__(1,2))
print("a"+"b")
print(str.__add__("a","b"))
print(len("shawki"))
print("shawki".__len__())

emp2.first="Boss"
print(emp2.fullname)
print(emp2.email)
print(emp2.first)

emp3.fullname="Mike Tyson"
print(emp3.first)
print(emp3.last)
print(emp3.email)

del emp3.fullname
