num1 = float(input('Number 1:'))
num2 = float(input('Number 2:'))
num3 = float(input('Number 3:'))

max = float('-inf') # very min num
if num1 > max:
    max = num1
#
if num2 > max:
    max = num2
#
if num3 > max:
    max = num3
#

print(f'Number 1 :{num1}')
print(f'Number 2 :{num2}')
print(f'Number 3 :{num3}')
print(f'Max :{max}')