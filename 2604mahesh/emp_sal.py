# for given basic sal
# hra %
# da %
# ta %
# find net salary
# and check net salary is 6-digit salary or not 

basic_salary = float(input('basic salary:'))
hra_per = float(input('HRA%:'))
da_per = float(input('DA%:'))
ta_per = float(input('TA%:'))

hra = (basic_salary / 100) * hra_per
da = (basic_salary / 100) * da_per
ta = (basic_salary / 100) * ta_per

net_salary = basic_salary + hra + da + ta 
print(f'Basic Salary:{basic_salary}')
print(f'HRA:{hra}')
print(f'DA:{da}')
print(f'TA:{ta}')
print(f'Net Salaryh:{net_salary}')

if net_salary > 100000:
    print('Net salary is 6-digt')
else:
    print('Net salary is not 6-digit')

