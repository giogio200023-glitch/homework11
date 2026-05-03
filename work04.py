###############
#1
n = input("write positive number:")
n = int(n)

while n >= 1:
    print(n)
    n -= 1
print("##########")

###############
# 2
###############


number = ""
total = 0
n = 0

while number != n:

   number = int(input("Enter a positive number:"))

   if number != n:

       print("try again")

   total += number


print(total)


#####################
# 3

secret_number = 7
while secret_number == 7:
    user_number = (input("Enter a number:"))

    if user_number == "quit":
        break
    if int(user_number) < 7:
        print("Too low")
    elif int(user_number) > 7:
        print("Too high")
    else:
        secret_number = user_number
        print("Correct!")

#############
# 4



user_word = input("enter your word:").strip().lower()

abc = ("a, e, i, o, u")

for word in user_word:

    if word in abc:

        continue

    print(word, end="")
print()



####
#5
# ვეცადე ერთ ფორში მომექცია ან ციკლში მაგრამ ვერ გავიგე როგორ გამეკთებიანა
# for a in range(0, 10):
#
#    for b in range(5, 16):
#
#        for c in range(0, 21,2):
#
#            for d in range(10, 0, -1):
#                print(f"{a} {b} {c} {d}", end="")

# one = range(0, 10)
# two = range(5, 16)
# three = range(0, 21, 2)
# four = range(10, 0 ,-1)
# on = (f" {one} {two} {three} {four}")
# print(on)
# print(one)

for a in range(0, 10):
    print(a, end="")
print()

for b in range(5, 16):
    print(b, end="")
print()

for c in range(0, 21,2):
    print(c, end="")
print()

for d in range(10, 0, -1):
    print(d, end="")
print()


