#  File: employee.py
#  Description: We created multiple different classes and sub classes. 
#  The sub classes inherit some properties from their parent classes which 
#  we were able to incorporate using super().
#  Student Name: Viren Govn
#  Student UT EID: vmg984
#  Partner Name: Diya Sharma
#  Partner UT EID: das5954
#  Course Name: CS 313E
#  Unique Number:
#  Date Created: 2/9/2023
#  Date Last Modified: 2/9/2023

import sys

class Employee:

    def __init__(self, **kwargs):
    # Add your code here!
        # result = ''
        # for key, value in kwargs.items():
        #     print(key, value)
        self.name = kwargs.get('name',"NULL")
        self.id = kwargs.get('id',"NULL")
        self.salary = kwargs.get('salary', 0)


    def __str__(self):
    # Add your code here!
        return f"{self.name},{self.id},{self.salary}"

############################################################
############################################################
############################################################

class Permanent_Employee(Employee):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.benefits = kwargs.get('benefits',[])

    def cal_salary(self):
        if self.benefits == ["health_insurance"]:
            return self.salary *.9
        elif self.benefits == ["retirement"]:
            return self.salary *.8
        elif self.benefits ==["retirement", "health_insurance"]:
            return self.salary *.7


    def __str__(self):
        return f'{super().__str__()}, {self.benefits}'


############################################################
############################################################
############################################################

class Manager(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bonus = kwargs.get('bonus',0)

    def cal_salary(self):
        return self.salary + self.bonus

    def __str__(self):
        return f'{super().__str__()}, {self.bonus}'


############################################################
############################################################
############################################################
class Temporary_Employee(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hours = kwargs.get('hours', 0)

    def cal_salary(self):
        return self.salary*self.hours

    def __str__(self):
        return f'{super().__str__()}, {self.hours}'

############################################################
############################################################
############################################################


class Consultant(Temporary_Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.travel = kwargs.get('travel',0)

    def cal_salary(self):
        return self.salary*self.hours + self.travel * 1000

    def __str__(self):
        return f'{super().__str__()}, {self.travel}'
############################################################
############################################################
############################################################


class Consultant_Manager(Manager, Consultant):
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)

    def cal_salary(self):
        return self.salary*self.hours + self.travel*1000 + self.bonus
    def __str__(self):
        return f'{super().__str__()}'


############################################################
############################################################
############################################################



###### DO NOT CHANGE THE MAIN FUNCTION ########

def main():

    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")

    emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:",  matt.cal_salary(), "\n")

if __name__ == "__main__":
  main()
