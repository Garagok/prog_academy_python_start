height = int(input('Enter height: '))
width = int(input('Enter width: '))

i = 1

while i <= height:
    j = 1
    while j <= width:
        if i == 1 or i == height:
            print('*', end = '')
        if 1 < i < height and 1 < j < width:
            print(" ", end = '')
        if 1 < i < height:
            if j == 1 or j == width:
                print('*', end = '')
        j = j + 1
    print()
    i = i + 1
