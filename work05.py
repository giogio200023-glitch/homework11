############
# 1
############

number_list = [3, 4, 5, 8, 2, 1]

sum = 0

for i in number_list:
    sum += i

print(sum)

############
# 2
############
# ამ დავალებას თავიდან ვერ მივხდი როგორ გამეკეთებია მაგრამ ინტერნეტი დავიხმარე და გავიზრე
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

max_number = numbers[0]
min_number = numbers[0]

for i in numbers:

    if max_number < i:
        max_number = i

    if min_number > i:
        min_number = i


print(max_number)

print(min_number)

print(numbers)

############
# 3
############


random_number = [2, 21, 24, 70, 98, 150, 3, 12, 7, 65, 27, 43, 83]

even = []
odd = []


for i in random_number:
    if i % 2 == 0:
        even.append(i)
    if i % 2 != 0:
        odd.append(i)


print(even)
print(odd)
print(random_number)


############
# 4
############

random_number_lst = [2, 21, 24, 70, 98, 150, 3, 12, 7, 65, 27, 43, 83,]

tuple_number = tuple(random_number_lst)

print(tuple_number)
print(random_number_lst)
print(type(random_number_lst))
print(type(tuple_number))

############
# 5
############

lst = [1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]
set = set(lst)

print(set)
print(lst)
