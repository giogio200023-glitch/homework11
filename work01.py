##############
#1
my_dog_name = "beni"
my_dog_is_boy = True
my_dog_age = 10
my_dog_food_price = 170.5

print(type(my_dog_is_boy))
print(type(my_dog_age))
print(type(my_dog_food_price))
print(type(my_dog_name))
#2
year = input("Enter a birth year:")
year = int(year)
year = 2025 - year
print("Your age around:", year)
#3
number = input("Enter random number: ")
number = int(number)
negative = number < 0
positive = number > 0
zero = number == 0
even = number % 2 == 0
odd = number % 2 != 0

print("Negative:", negative)
print("Positive:", positive)
print("Zero:", zero)
print("Even:", even)
print("Odd:", odd)

