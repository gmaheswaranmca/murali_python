num = int(input('Number:'))

# is num a prime? yes or no

isPrime = True  
for iNum in range(2,num): # between 2 and before num ie 2..num-1 ->2,3,4,5,..,num-1
    if num % iNum == 0:
        isPrime = False 
        break
    #
#

if isPrime:
    print(f'{num} is prime number')
else:
    print(f'{num} is not prime number')
