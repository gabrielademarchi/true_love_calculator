print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name_combination = name1.lower() + name2.lower()

dozens = name_combination.count('t') + name_combination.count(
    'r') + name_combination.count('u') + name_combination.count('e')

units = name_combination.count('l') + name_combination.count('o') + \
    name_combination.count('v') + name_combination.count('e')

love_score = int(str(dozens)+str(units))

if (love_score < 10 or love_score > 90):
    print(f'Your score is {love_score}, you go together like coke and mentos.')
elif (love_score > 40 and love_score < 50):
    print(f'Your score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}.')
