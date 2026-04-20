import math 
num = 1.235728
print(f'num={num:.2f}') #1.24
num1 = num * 100 #123.5728
num2 = math.floor(num1) #123
num_result = num2 / 100 #1.23
print(f'num_result={num_result:.2f}') 

num_display = math.floor(num * 100) / 100 # 123.5728 -> 123 -> 1.23
print(f'num_display={num_display:.2f}')