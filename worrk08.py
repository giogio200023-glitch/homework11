# 1. დაწერე ფუნქცია sum_of_digits(n), რომელიც რეკურსიულად ითვლის რიცხვის ციფრების ჯამს.
#    მაგ: sum_of_digits(1234) → 10 (1+2+3+4)
#    გაითვალისწინეთ, რიცხვები არ უნდა გადაეწოდოს ცალ-ცალკე არგუმენტად, უნდა გადაეცეს მხოლოდ ერთი
#



def sum_of_digits(num: int): # ლექციაზე დავწერეთ
    if num == 0:
        return 0
    nashti = num % 10
    return nashti + sum_of_digits(num // 10) # რეკურსია

sum_of_digits = sum_of_digits(1234)
print(sum_of_digits)



# 2. შექმენი lambda ფუნქცია is_even, რომელიც ამოწმებს რიცხვი ლუწია თუ არა და აბრუნებს True ან False.

is_even = lambda x: x % 2 == 0

print(is_even(7))
print(is_even(8))


# 3. მოცემულია ლისტი:
#     students = [
#     ("Luka", 15, 85),
#     ("Ana", 14, 92),
#     ("Giorgi", 16, 78),
#     ("Nino", 15, 95)
# ]
#
# დაასორტირეთ:
#     ჯერ ასაკის მიხედვით,
#     თუ ასაკი ტოლია — ქულის მიხედვით.
#     გამოიყენე lambda.

#
# students = [
#     ("Luka", 15, 85),
#     ("Ana", 14, 92),
#     ("Giorgi", 16, 78),
#     ("Nino", 15, 95)
# ]
#
# students_list = sorted(students, key=lambda x: (x[1], x[2]))# ქულებით როგორ დამეხარსიხებია თუ ტოლი იქნებოდა ვერ მიხვდი if ს გამოყენებას ვცდილობდი მაგრამ არ გამომივიდა
#
#
# for student in students_list:
#     print(student)


# 4. მოცემულია ლისტი:
words = ["banana", "apple", "kiwi", "watermelon", "cherry"]
# დაასორტირეთ სიტყვის სიგრძის მიხედვით, კლებადობით


words_len = sorted(words, key=lambda x: len(x), reverse=True)

print(words_len)



# 5. დავალება 4-ში მოცემულ ლისტში, თითოეული სიტყვის პირველი ასო გადააკონვერტირეთ მაღალ რეგისტრში,
# გამოიყენეთ map ფუნქცია

capital_words = list(map(lambda x: x.title(), words))

print(capital_words)


# 6. მოცემულია ლისტი:
numbers = [5, 12, 7, 18, 3, 24, 9]
# ამოიღე მხოლოდ ის რიცხვები, რომლებიც 10-ზე მეტია და 3-ზე გაყოფილია უნაშთოდ.
# გამოიყენე filter ფუნქცია
num = list(filter(lambda x: x > 10 and x % 3 == 0, numbers))
print(num)