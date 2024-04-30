class Person:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getMajor(self):
        return self.major

class Employee(Person):
    def __init__(self, name, age, employeeID,major):
        super().__init__(name, age, major)
        self.employeeID = employeeID

    def getID(self):
        return self.employeeID


# Employee 클래스를 이용하여 객체 생성
employee = Employee("Chae Rin", 23, 2021, "Internet of Things")

# 객체의 이름, 나이, ID 출력
print("Name:", employee.getName())
print("Age:", employee.getAge())
print("ID:", employee.getID())
print("Major:", employee.getMajor())
