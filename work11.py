########
#1
########


def my_decorator (func):
    def wrapper(a,b):
        if a < 0 or b < 0:
            return "only positive numbers allowed"
        return func(a,b)
    return wrapper


@my_decorator
def add(a,b):
    return a+b

@my_decorator
def subtract(a, b):
    return a - b

@my_decorator
def multiply(a, b):
    return a * b

@my_decorator
def divide(a,b):
    if b == 0:
        return "cannot divide by zero!"
    return a / b

print(add(3,4))
print(add(-3,4))
print(subtract(3,4))
print(multiply(3,4))
print(divide(3,4))
print(divide(5,0))
print(multiply(0,5))





#########
#2
#########


def decorator(func):
    def wrapper(num1, num2):
        result = func(num1, num2)
        print(f"called function '{func.__name__}', with attributes {num1} and {num2}, returned {result}")
        return result
    return wrapper


@decorator
def add(num1, num2):
    return num1 + num2


@decorator
def multiply(num1, num2):
    return num1 * num2

@decorator
def divide(num1, num2):
    if num2 == 0:
        return "cannot divide by zero!"
    return num1 / num2

@decorator
def subtract(num1, num2):
    return num1 - num2


add(10, 15)
multiply(4, 5)
subtract(10, 15)
divide(4, 5)




#######
#3
#######
# ეს ჩემით ვერ გავიგე როგორ გამეკეთებია თავიდან დელეი როგორ ამეწყო მომიწია ხელოვნური ინტელექტი დამეხმარებინა
import time

def repeat(times, delay):
    def m_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)
                if i < times - 1:
                    time.sleep(delay)
        return wrapper
    return m_decorator


@repeat(times=3, delay=2)
def greet(name):
    print("hello, " + name)


greet("Giorgi")




#######
# 4
#######

# ეს ვერ გავიგე დიდად ან უბრალოდ შეიძლება ბევრი ინფორმაციაა და ცოტა გავჭედე

