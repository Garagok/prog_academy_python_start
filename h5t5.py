list_a = [0, 5, 2, 4, 7, 1, 3, 19]

count = 0

for elem in list_a:
    if elem % 2 != 0:
        count = count + 1
print(count)
