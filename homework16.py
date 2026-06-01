####################
#1
print("#####"*10,"\n No1. ","\n")
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self):
        return f"{self.first_name} {self.last_name}"

class Student(Person):
    def introduce(self):
        return f"Student:{self.first_name} {self.last_name}."


class Lecturer(Person):
    def introduce(self):
        return f"Lecturer:{self.first_name} {self.last_name}."


lecturer = Lecturer("John", "Doe")
lecturer1 = Lecturer("Giorgi", "Kutchukhidze")

print(lecturer.introduce())
print(lecturer1.introduce())

student = Student("Jane", "Doe")
student1 = Student("inga","Phutkaraze")

print(student1.introduce())
print(student.introduce())

print("#####"*10)


############################
#2
print("#####"*10,"\n No2. ","\n")

class Profile:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  #__ privati

    def check_password(self, password):
        if self.__password == password:
            return "Correct password"
        else:
            return "Wrong password"

    def change_password(self, old_password, new_password):
        if self.__password == old_password:
            self.__password = new_password
            return "New password updated"
        else:
            return "Old password is not correct"



profile = Profile("giogio200023", "12345678")

print(profile.check_password("1234567")) # araswori paroli
print(profile.check_password("12345678"))# swori paroli

print(profile.change_password("1234567", "giogio")) #araswori parolis shecvlis mcdeloba
print(profile.change_password("12345678", "giogio"))# swori parolis shecvla

print(profile.check_password("giogio"))  # shemowmeba sheicvala tu ara

print("#####"*10)


#######################
#3
print("#####"*10,"\n No3. ","\n")


class Product:

    def __init__(self, fruit, price):
        self.fruit = fruit
        self.__price = None
        self.set_price(price)

    def set_price(self, price):
        try:

            if price < 0:
                raise ValueError(f"Price can't be negative: {price}")

           # if price == None
           #     raise TypeError("Price can't be None")  როგორ გავაკეთო ისე რომ თუ ფასი საერთოდ არ მიუთითა ტაიპ ერორი დაწეროს

            self.__price = price
            print(f"Price update: {self.__price}")

        except (TypeError, ValueError) as e:
            print(e)# იმის და მიუხედავად რომ პრინტ ე მიწერია და შეცდომაა -10 ვუთითედ ეს არ მიწერს ვერ გავიგე როგორ გამოვაჩინო


    def get_price(self):
        return self.__price


product = Product("apple", 1.5)

print(f"fruit: {product.fruit}")
print(f"price: {product.get_price()}")

print()

product.set_price(2)
print(f"price: {product.get_price()}")

product.set_price(-10)


print("#####"*10)

#########################
#4
print("#####"*10,"\n No4. ","\n")


class Payment:
    def pay(self, amount):
        return

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"creditcard pay: {amount}")


class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"paypal pay: {amount}")


class CryptoPayment(Payment):
    def pay(self, amount):
        print(f"crypto pay: {amount}")


paypal = PayPalPayment()
creditcard = CreditCardPayment()
cryptopay = CryptoPayment()

paypal.pay(100)
creditcard.pay(100)
cryptopay.pay(100)

print("#####"*10)

#############################
#5
print("#####"*10,"\n No5. ","\n")


class Car:
    total_cars = 0

    def __init__(self, brand):
        self.brand = brand
        Car.total_cars += 1

    def get_total_cars(): # აქ ვერ გავიგე რატო აწითლებს
        return f"all car brands: {Car.total_cars}"



car1 = Car("Toyota")
car2 = Car("BMW")
car3 = Car("Mercedes")
car4 = Car("Ford")
car5 = Car("Honda")
car6 = Car("Tesla")
car7 = Car("Audi")

print(Car.get_total_cars())


print("#####"*10)