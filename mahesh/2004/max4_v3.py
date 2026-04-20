num1 = float(input('Number 1:')) # 20
num2 = float(input('Number 2:')) # 25
num3 = float(input('Number 3:')) # 10
num4 = float(input('Number 4:')) # 15

nums = [num1, num2, num3, num4]
max = float('-inf')#0 
for eNum in nums:
    if eNum > max:
        max = eNum 
    #

print(f'Number 1 :{num1}')
print(f'Number 2 :{num2}')
print(f'Number 3 :{num3}')
print(f'Number 4 :{num4}')
print(f'Max :{max}')