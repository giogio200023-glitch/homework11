############
#1
name = input("Please enter your full name:")
name = name.split()#split ფუნქციის გამოყენება არ იყო წესიერად ახსნილი ამიტომ გუგლი დავიხმარე რომ გამეგო როგორ მუშაობდა
name1 = name[0][0]
name2 = name[1][0]

print(f"Your initials are:{name1.upper()}.{name2.upper()}.")

###########
# 2
word = input("write random word")
print(word[::-1])

###########
# 3
sentence = input("Plase write Sentence:")
change = input("Write me two words.\n The first word will be from your sentence and the second word will be \n what you want to replace the first word with:")
change =change.split()
change1 = change[0]
change2 = change[1]
sentence = sentence.replace(change1, change2)
print(sentence)