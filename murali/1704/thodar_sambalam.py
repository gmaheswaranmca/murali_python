def calculate_salary():
    adipadai_sambalam = float(input('adipadai sambalam:'))
    vethu_salukai_per =  float(input('vethu salukai%:'))
    daily_salukai_per = float(input('daily salukai%:'))
    payana_salukai_per = float(input('payana salukai%:'))

    vethu_salukai = (adipadai_sambalam/100)*vethu_salukai_per 
    daily_salukai = (adipadai_sambalam/100)*daily_salukai_per  
    payana_salukai = (adipadai_sambalam/100)*payana_salukai_per

    nikara_sambalam = adipadai_sambalam + vethu_salukai + daily_salukai + payana_salukai
    print(f'adipadai sambalam:{adipadai_sambalam}')
    print(f'vethu salukai : {vethu_salukai}')
    print(f'daily salukai : {daily_salukai}')
    print(f'payana salukai : {payana_salukai}')
    print(f'nikara sambalam : {nikara_sambalam}')

    if nikara_sambalam > 100000:
        print('nikara sambalam is 6 digit')
    else:
        print('nikara sambalam is not 6 digit')

#
print('welcome to the sambalam kanaku seium app')
choice = 'y'
while choice == 'y':
    calculate_salary ()
    choice = input('do you want countine(y/n)?')
#
print('nandri for using the sambalam kanaku seium app')