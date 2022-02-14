import math

radius = int(4)
x = int(input('Enter x: '))
y = int(input('Enter y: '))

hypotenuse = math.sqrt(x ** 2 + y ** 2)

if hypotenuse <= radius:
    print('Coordinate is inside the circle')
else:
    print('Coordinate is outside the circle')
