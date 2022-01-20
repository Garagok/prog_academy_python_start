# Existing triangle task
a = int(input('Enter value for a: '))
b = int(input('Enter value for b: '))
c = int(input('Enter value for c: '))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print('This triangle exists')
else:
    print('This triangle does not exist')
