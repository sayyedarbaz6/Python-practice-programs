class Student:

    def __init__(self):
        self.roll = input("Enter your Roll number:")
        self.name = input("Enter your name:")
        self.percent = int(input("Enter your Percentage:"))
class Test(Student):
    def display(self):
        print("============ Student info is ==========")
        print("Rollno \tName \tPercentage")
        print("",self.roll,"\t",self.name,"\t",self.percent)
obj = Test()
obj.display()