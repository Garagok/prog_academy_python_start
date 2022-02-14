ticket = int(input('Enter a four-digit number: '))

n1 = ticket // 1000
n2 = ticket % 1000 // 100
n3 = ticket % 100 // 10
n4 = ticket % 10 // 1

if (n1+n2) == (n3+n4):
    print('This ticket is lucky')
else:
    print('This ticket is unlucky')
