def circle_area(radius):
    pi = 22 / 7
    area = pi * (radius ** 2)
    return area 

# 
r1 = 50
a1 = circle_area(r1)

print(f'radius of circle:{r1}')
print(f'area of circle:{a1:.2f}')

r2 = 400
a2 = circle_area(r2)

print(f'radius of circle:{r2}')
print(f'area of circle:{a2:.2f}')