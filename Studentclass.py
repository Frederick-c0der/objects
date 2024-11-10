class Student():
    def __init__(self):
        self.name=""
        self.age=0
        self.house=""
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("House:", self.house)
    def change(self):
        self.name=input("Input Name")
        self.age=input("Input Age")
        int(self.age)
        self.house=input("Input House")
Luke=Student()
Leia=Student()
Luke.change()
Luke.display()
