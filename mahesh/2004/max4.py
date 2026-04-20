num1 = int(input('Number 1:'))
num2 = int(input('Number 2:'))
num3 = int(input('Number 3:'))
num4 = int(input('Number 4:'))

if num1 > num2 and num1 > num2 and num1 > num3:
    max = num1
elif num2 > num3 and num2 > num4:
    max = num2 
elif num3 > num4:
    max = num3
else:
    max = num4

print(f'Number 1 :{num1}')
print(f'Number 2 :{num2}')
print(f'Number 3 :{num3}')
print(f'Number 4 :{num4}')
print(f'Max :{max}')