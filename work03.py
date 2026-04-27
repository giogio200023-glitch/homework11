#######################
# 1 #
user_age = input("please enter your age:")
user_age = int(user_age)
if user_age <= 12:
    print("kid")
elif user_age <= 19:
    print("teenager")
elif user_age <= 64:
    print("adult")
else:
    print("elder")

# 2 #
student_score = input("Enter your score 0-100:")
student_attendance = input("Enter your attendance percent 0%-100%:")


student_attendance = int(student_attendance.replace("%", ""))#პროცენტით ვერ გავიგე როგორ მექნა ამიტომ მოვიძიე ინტერნეტში და ისე ვქენი(თუ პროცენთი დაწერს პროცენტი წაიშლება, ან თუ არ დაწერს პროცენთი არც ეგ იქნება პრობლემა)
student_score = int(student_score)

if student_score >= 60 and student_attendance >= 75:
    print(f"You score are {student_score},{student_attendance}%,You Passed")
else:
    print(f"Your score are {student_score},{student_attendance}%,You did not pass")

# 3 #

student = input("Are you a student ? Yes/No:")
member = input("Are you a member ? Yes/No:")

student = student.lower()
member = member.lower()

if student == "yes"and member == "yes":
    print("You have an additional discount")
elif student == "yes" or member == "yes":
    print("You have a discount")

else:
    print("You have no discount")


# 4 #
# ეს პირველი ვარიანტი ( დამატებული აქ მიწერა ან გრძელია ან მოკლეა username)
# username = input("Enter your username:")
# username1 = (len(username))
#
# if username1 < 3:
#     print("Your username to short")
# elif username1 > 20:
#     print("Your username to long")
# else:
#     username = username.isalnum()
#     if username == True:
#         print("Your username is correct ")
#     else:
#         print("Your username is incorrect ")
#


username = input("Enter your username:")
username1 = (len(username))

if 20 >= username1 >= 3:
    username = username.isalnum()
    if username:
        print("username is valid")
    else:
        print("username is invalid")


else:
    print("username is invalid")