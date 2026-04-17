# for given age, classify the person as child, teenager, adult, middle man/woman, old man/woman, very old man/woman
def categorize_age():
    age = int(input('age:'))
    if age <= 12: 
        print('you are child')
    elif age <= 19:
        print('you are teenager')
    elif age <= 40:
        print('you are adult')
    elif age <= 60:
        print('you are middle aged adult')
    elif age <= 80:
        print('you are senior citizen')
    else:
        print('you are super senior citizen')
#
print('Welcome to age classifier app!!!')
choice = 'y'
while choice == 'y':
    categorize_age()
    choice = input('do you continue(y/n):')
#
print('Thank you for using age classifier app')