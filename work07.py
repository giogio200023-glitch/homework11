# 1.დაწერე ფუნქცია find_min_max, რომელიც მიიღებს ნებისმიერი რაოდენობის რიცხვებს (*args) და დააბრუნებს:
#
# ყველაზე პატარა რიცხვს
# ყველაზე დიდ რიცხვს
def find_min_max(*args):

  return min(args), max(args)


minimum, maximum = find_min_max(1,2,3,4,5,6)
print(minimum)
print(maximum)


# 2.დაწერე ფუნქცია calculate, რომელიც:
#
# იღებს *args
# იღებს keyword არგუმენტს operation
#
# operation შეიძლება იყოს:
#
# "sum"  → ჯამი
# "max"  → მაქსიმუმი
# "min"  → მინიმუმი
# "mult" → ნამრავლი

def calculate(*args, operation):
  if operation == "sum":
      return sum(args)
  elif operation == "min":
      return min(args)
  elif operation == "max":
      return max(args)
  elif operation == "mult":
      multi_result = 1
      for i in args:
          multi_result *= i
      return multi_result
  else:
      print("Invalid operation")

# calculate(1,2,3,4,5,6,operation="sum")# თავიდან ასე გავაკეთე მაგრამ არ გამომივიდა უბრალოდ მისამართს მიწერდა ოპერატიულ მეხსიერებაში სად იყო
# print(calculate)

print(calculate(1, 2, 3, 4, 5, operation="sum"))# ხელოვნური ინტელექტი დავიხმარე
print(calculate(1, 2, 3, 4, 5, operation="max"))
print(calculate(1, 2, 3, 4, 5, operation="min"))
print(calculate(1, 2, 3, 4, 5, operation="mult"))


# 3.დაწერე ფუნქცია format_user, რომელიც იღებს:
#
# first_name
# last_name
# **kwargs
#
# და აბრუნებს სტრინგს ამ ფორმატში:
#
# format_user("John", "Doe", age=25, job="Developer")
# John Doe | age: 25, job: Developer


def format_user(first_name, last_name, **kwargs):
    full_name = f"{first_name} {last_name}"

    more_info = ""
    for key, value in kwargs.items():
        more_info += f"{key}: {value}"

    return f"{full_name} | {more_info}"

print(format_user(first_name="John", last_name="Smith", age=25, job="Developer"))
## John Doe | age: 25, job: Developer ესეთი ვერ გამოვიყვანე მძიმე როგორ დამესვა შუაში ვერ გავიგე


# 4. დაწერე ფუნქცია safe_divide(a, b), რომელიც:
#
# თუ b == 0 → აბრუნებს "Cannot divide by zero"
# სხვა შემთხვევაში აბრუნებს:
# მთელ ნაწილს და ნაშთს, ორივეს ერთად
#
# safe_divide(10, 2)  # (5, 0)
# safe_divide(10, 0)  # Cannot divide by zero


def safe_divide(a,b):
    if b == 0:
        return "cannot divide by zero"
    else:
        return (a // b, a % b)
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, 1))
print(safe_divide(10, 3))