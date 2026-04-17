# adipadai salary
# vethu vadakai salukai%
# daily salukai%
# payana salukai%
# nikara sambalam
# to check wheather the nikara sambalam is greater than 6 digt

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
