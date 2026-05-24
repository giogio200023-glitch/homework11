# 1. ლისტიდან უსაფრთხო წვდომა
# შექმენი ფუნქცია safe_get(lst, index), რომელიც იღებს სიას და ინდექსს.
#
# თუ ინდექსი არასწორია (IndexError), დაბეჭდე:
# "Error: There is no item with this index"
# თუ ინდექსი არ არის რიცხვი (TypeError), დაიჭირე შეცდომა.

def safe_get(lst, index):
    try:
        return lst[index]
    except IndexError:
        print("Error: There is no item with this index")
    except TypeError:
        print("type error")
    finally:
        print("all done")


number_lst = [1,2,3,4,5,6,7,8,9]

print(safe_get(number_lst, 0,))
print(safe_get(number_lst, 1))
print(safe_get(number_lst, 9))
print(safe_get(number_lst, "error"))
print("######"*10)

# ეს None რატო იწერება ?




############################################################


# 2. დიქტიდან უსაფრთხო წვდომა
# შექმენი ფუნქცია safe_get_value(dictionary, key).
#
# თუ გასაღები არ არსებობს (KeyError), დაბეჭდე:
# "Error: Key '{key}' doesn't exist"
# დააბრუნე მნიშვნელობა ან None.



def safe_get_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        print(f"Error: Key '{key}' doesn't exist")
        return None


uni_info = {
    "name": "Giorgi",
    "age": 26,
    "city": "Kutaisi"
}

print(safe_get_value(uni_info, "name"))
print(safe_get_value(uni_info, "age"))
print(safe_get_value(uni_info, "mail"))

print("######"*10)

################################################


# 3. რიცხვის კვადრატი მომხმარებელს შემოატანინე რიცხვი და დაბეჭდე მისი კვადრატი.
#
# გამოიყენე:
#
# try — რიცხვის მისაღებად
# except — თუ მომხმარებელი არასწორ მონაცემს შეიყვანს
# else — შედეგის დასაბეჭდად
# finally — ტექსტისთვის "ოპერაცია დასრულებულია"

try:
    number = int(input("input number: ")) # მთელი რიცხვები ჩავსვი მაგრამ int მაგივრად floats თუ დავწერ ნებისმიერიზე იზამს
except ValueError:
    print("Error: Please input a number")
else:
    print(f"{number} square = {number ** 2}")
finally:
    print("all done")


print("######"*10)