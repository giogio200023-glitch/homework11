##########################################
#1
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof!")

    def info(self):
        print(f"Name: {self.name}, age: {self.age}")


my_dog = Dog("beni", 11)
my_dog.info()
my_dog.bark()
print("######"*10)



##########################################
#2
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height



r1 = Rectangle(6, 6)
print("area =",r1.area())
print("perimeter =",r1.perimeter())
print(r1.is_square())


r2 = Rectangle(5, 6)
print("area =",r2.area())
print("perimeter =",r2.perimeter())
print(r2.is_square())
print("######"*10)

##########################################
#3

class BankAccount:
    bank_name = "Step Bank"

    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"add {amount}GEl. new balance: {self.balance}GEL")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"take {amount}Gel. new balance: {self.balance}GEL")

    def show_balance(self):
        print(f"bank: {BankAccount.bank_name} | owner: {self.owner} | balance: {self.balance}GEL")


# ტესტირება
giorgi = BankAccount("giorgi", 100)
inga = BankAccount("inga", 1.5)

giorgi.show_balance()
giorgi.deposit(200)
giorgi.withdraw(50)
giorgi.withdraw(500)
giorgi.show_balance()

print()

inga.show_balance()

print("######"*10)


##########################################
#4
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def average(self):
        total = sum(s.grade for s in self.students)
        return round(total / len(self.students), 2)

    def top_student(self):
        best = max(self.students, key=lambda s: s.grade)
        return best.name



classroom = Classroom()

classroom.add_student(Student("Giorgi", 8))
classroom.add_student(Student("Inga", 10))
classroom.add_student(Student("Nino", 7))
classroom.add_student(Student("Beqa", 9))

print(classroom.average())
print(classroom.top_student())