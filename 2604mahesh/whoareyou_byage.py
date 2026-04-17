# for given age, classify the person as child, teenager, adult, middle man/woman, old man/woman, very old man/woman
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

    
