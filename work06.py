# 1. შექმენით ლისტი, რომელშიც ზოგიერთი ელემენტი იქნება განმეორებული,
# დაწერეთ ლოგიკა, რომელიც დაითვლის თუ რამდენჯერ არის თითოეული სიტყვა მოხსენიებული წინადადებაში.
# გამოიყენეთ dict რაოდენობის დასათვლელად და საბოლოოდ დაბეჭდეთ dict.
# მინიშნება: key მნიშვნელობებად შეინახეთ ლისტში არსებული ელემენტები, მისი value კი აღნიშნეთ რიცხვით
#
# 2. შექმენით ორი dict, რომელთაც ზოგიერთი key მნიშვნელობა ექნება ერთი და იგივე.
# გააერთიანეთ ეს ორი dict, თუ key მნიშვნელობები ერთმანეთს დაემთხვევა, მაშინ value მნიშვნელობებით შექმენით ლისტი და ეს ლისტი დაამატეთ როგორც value ახალ dict-ში
#
# 3. შექმენით dict და დააგენერირეთ მისი შებრუნებული ვერსია(key <-> value), მაგალითად:
# თუ გვაქვს dict: {'a': 1, 'b': 2, 'c': 3}
# შებრუნების შედეგად უნდა მიიღოთ შედეგი: {1: 'a', 2: 'b', 3: 'c'}
#
# 4. გაქვს ორი სეტი, რომლებიც შეიცავს ფილმებს, რომლებიც უყვართ ორ სხვადასხვა ადამიანს:
# films1 = {"Inception", "Interstellar", "Joker", "The Matrix", "Dune", "Oppenheimer"}
# films2 = {"Joker", "The Matrix", "Parasite", "Interstellar", "The Shawshank Redemption", "Dune"}
#
# დაბეჭდე შემდეგი ინფორმაცია:
# საერთო ფილმები (ორივეს უყვარს)
# ფილმები, რომლებიც უყვარს მხოლოდ პირველ ადამიანს (films1-ში)
# ფილმები, რომლებიც უყვარს მხოლოდ მეორე ადამიანს (films2-ში)
# ყველა უნიკალური ფილმი (ორივე სეტის გაერთიანება)
#
#
# 5. დავალების შესასრულებლად info.json ფაილში არსებული ინფორმაცია გადმოიტანეთ პითონის ფაილში და შეინახეთ ცვლადში
#
#    1. დაბეჭდე ყველა სტუდენტის სახელი და მისი საშუალო ქულა.
#    2. იპოვე საუკეთესო სტუდენტი სკოლაში (ყველაზე მაღალი საშუალო ქულით).
#    3. დაბეჭდე ყველა სტუდენტი, რომლებსაც აქვთ დასწრება 90%-ზე მეტი.
#    4. იპოვე რომელ კლასში არის ყველაზე მეტი სტუდენტი.
#    5. დაბეჭდე ყველა სტუდენტი, რომელიც დადის პროგრამირებაზე.
#    6. გამოთვალე საშუალო დასწრება მთელ სკოლაში.
#    7. შექმენი ახალი ლექსიკონი, სადაც გასაღები იქნება სტუდენტის სახელი, ხოლო მნიშვნელობა — მისი საგნების რაოდენობა.
#    8. იპოვე სტუდენტი, რომელსაც აქვს ყველაზე მეტი დამატებითი აქტივობა.


##
# 1
##

user_names = ("mariami","levani","nika","lasha","giorgi","mariami","levani","nika","lasha","giorgi","tatia","gela")

number_of_users = {}

for user in user_names:
    if user in number_of_users:
        number_of_users[user] += 1
    else:
        number_of_users[user] = 1
print(number_of_users)

##
# 2
##
# 2. შექმენით ორი dict, რომელთაც ზოგიერთი key მნიშვნელობა ექნება ერთი და იგივე.
# გააერთიანეთ ეს ორი dict, თუ key მნიშვნელობები ერთმანეთს დაემთხვევა, მაშინ value მნიშვნელობებით შექმენით ლისტი და ეს ლისტი დაამატეთ როგორც value ახალ dict-ში

# ცოტა პირობა ვერ გავიგე იმედია სწორად არის
dict1 = {"name":"giorgi", "age":26, "city": "Kutaisi"}
dict2 = {"name":"inga", "age":22, "country": "Georgia"}

mix = {}
lst = {dict1["city"],dict2["country"]}
for key, value in dict1.items():
    mix[key] = value

for key, value in dict2.items():
    if key in mix:
        mix[key] = [mix[key], value]
    else:
        mix[key] = value
print(mix)
print(lst)


##
#3
##
# 3. შექმენით dict და დააგენერირეთ მისი შებრუნებული ვერსია(key <-> value), მაგალითად:
# თუ გვაქვს dict: {'a': 1, 'b': 2, 'c': 3}
# შებრუნების შედეგად უნდა მიიღოთ შედეგი: {1: 'a', 2: 'b', 3: 'c'}

student_score = {"math": 92, "history": 67, "sport": 100}
score_student = {}

for key, value in student_score.items():
    score_student[value] = key


print(score_student)


##
# 4
##
# 4. გაქვს ორი სეტი, რომლებიც შეიცავს ფილმებს, რომლებიც უყვართ ორ სხვადასხვა ადამიანს:
# films1 = {"Inception", "Interstellar", "Joker", "The Matrix", "Dune", "Oppenheimer"}
# films2 = {"Joker", "The Matrix", "Parasite", "Interstellar", "The Shawshank Redemption", "Dune"}
#
# დაბეჭდე შემდეგი ინფორმაცია:
# საერთო ფილმები (ორივეს უყვარს)
# ფილმები, რომლებიც უყვარს მხოლოდ პირველ ადამიანს (films1-ში)
# ფილმები, რომლებიც უყვარს მხოლოდ მეორე ადამიანს (films2-ში)
# ყველა უნიკალური ფილმი (ორივე სეტის გაერთიანება)

films1 = {"Inception", "Interstellar", "Joker", "The Matrix", "Dune", "Oppenheimer"}
films2 = {"Joker", "The Matrix", "Parasite", "Interstellar", "The Shawshank Redemption", "Dune"}

print("love first user:",films1.difference(films2))# უყვარს მხოლოდ პირველს
print("both love:",films1.intersection(films2))#საერთო ფილმები
print("love second user:",films2.difference(films1))#უყვარს მხოლოდ მეორეს
print("unique:",films1.symmetric_difference(films2))#უნიკალური ფილმები

##
#5
##
##ეს დავალება ძაან გამიჭირდა ინტერნეტის გამოყენების გარეშე ვერ გავაკეთე, მათ შორის Ai ც გამოვიყენე რომ გამეგო რა როგორ
classes ={
  "class 10A": {
    "giorgi": {
      "age": 16,
      "average score": 8.7,
      "subjects": {
        "math": {"score": 9, "test": True},
        "physics": {"score": 8, "test": True},
        "history": {"score": 9, "test": True},
        "english": {"score": 10, "test": True}
      },
      "attendance": 92,
      "add": ["football", "programming"]
    },
    "ana": {
      "age": 15,
      "average score": 9.4,
      "subjects": {
        "math": {"score": 10, "test": True},
        "physics": {"score": 9, "test": True},
        "history": {"score": 8, "test": True},
        "english": {"score": 10, "test": True}
      },
      "attendance": 98,
      "add": ["dance"]
    },
    "david": {
      "age": 16,
      "average score": 7.2,
      "subjects": {
        "math": {"score": 6, "test": False},
        "physics": {"score": 7, "test": True},
        "history": {"score": 8, "test": True},
        "english": {"score": 9, "test": False}
      },
      "attendance": 75,
      "add": ["basketball", "programming"]
    }
  },
  "class 10B": {
    "mariam": {
      "age": 15,
      "average score": 9.1,
      "subjects": {
        "math": {"score": 9, "test": True},
        "biology": {"score": 10, "test": True}
      },
      "attendance": 95,
      "add": ["music", "art"]
    },
    "levan": {
      "age": 16,
      "average score": 6.8,
      "subjects": {
        "math": {"score": 5, "test": False},
        "physics": {"score": 7, "test": False}
      },
      "attendance": 60,
      "add": []
    }
  }
}



# 1. დაბეჭდე ყველა სტუდენტის სახელი და მისი საშუალო ქულა.
for  clas, students in classes.items():
    for student, student_score in students.items():

        print(f"{student} {student_score["average score"]}/ ",end="" )

print()


#2. იპოვე საუკეთესო სტუდენტი სკოლაში (ყველაზე მაღალი საშუალო ქულით).
best_student = ""
best_score = 0


for  clas, students in classes.items():
    for student, student_score in students.items():
      if student_score["average score"] > best_score:


        best_score = student_score["average score"]
        best_student = student

print(f"{best_student}:{best_score}")# ამ სტუდენტის სახელი როგორ მიმეგრებინა ვერ მივხდი


# 3. დაბეჭდე ყველა სტუდენტი, რომლებსაც აქვთ დასწრება 90%-ზე მეტი.
for class_name, students in classes.items():
    for student, student_score in students.items():


        if student_score["attendance"] > 90:

            print(f"{student}:{student_score['attendance']}%")
print()


#4. იპოვე რომელ კლასში არის ყველაზე მეტი სტუდენტი.
max_students = 0

for class_name, students in classes.items():
  if len(students) > max_students:

    max_students = len(students)
    print(f"{class_name}:{max_students}")
print()

#5. დაბეჭდე ყველა სტუდენტი, რომელიც დადის პროგრამირებაზე.
for class_name, students in classes.items():
  for student, student_score in students.items():

    if "programming" in student_score["add"]:
      print(f"{student}")
print()

#    6. გამოთვალე საშუალო დასწრება მთელ სკოლაში.
student_average = 0
student_total = 0
student_average_attendance = 0

for class_name, students in classes.items():
  for student, student_score in students.items():

    student_average += student_score["attendance"]
    student_total += 1

average_student_attendance = student_average / student_total
print(average_student_attendance)
print()

#    7. შექმენი ახალი ლექსიკონი, სადაც გასაღები იქნება სტუდენტის სახელი, ხოლო მნიშვნელობა — მისი საგნების რაოდენობა.
subject_name = {}
for class_name, students in classes.items():
  for student, student_score in students.items():

    subject_name[student] = len(student_score["subjects"])
print(subject_name)

print()
#    8. იპოვე სტუდენტი, რომელსაც აქვს ყველაზე მეტი დამატებითი აქტივობა
max_add = 0
best_student = ""

for class_name, students in classes.items():
    for student, student_score in students.items():

        if len(student_score["add"]) > max_add:
            max_add = len(student_score["add"])
            best_student = student

print(f"{best_student}: {max_add}")
