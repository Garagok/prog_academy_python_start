from math import sqrt    # Import square root from math library


a = int(input('A = '))  # A
b = int(input('B = '))  # B
c = int(input('C = '))  # C

print('Find semi-perimeter')
p = (a+b+c)/2   # Semi-Perimeter formula
print('p = ', p)

print('Find Area of our Triangle')
s = sqrt(p*(p-a)*(p-b)*(p-c))   # Area formula
print('S = ', s)
