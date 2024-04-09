class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


class Employee(Person):
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)
        self.employeeID = employeeID

    def getID(self):
        return self.employeeID


# Employee 클래스를 이용하여 객체 생성
employee = Employee("IoT", 65, 2018)

# 객체의 이름, 나이, ID 출력
print("이름:", employee.getName())
print("나이:", employee.getAge())
print("ID:", employee.getID())
