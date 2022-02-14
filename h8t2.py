arr_1 = []
arr_2 = []
arr_3 = []

for i in range(1, 100, 1):
    if i % 3 == 0: arr_1.append(i)
    if i % 5 == 0: arr_2.append(i)

print('List multiple of 3:', arr_1)

print('List multiple of 5:', arr_2)

m1 = set(arr_1)
m2 = set(arr_2)
m = m1.intersection(m2)

for i in m:  arr_3.append(i)
print('List with common elements:', arr_3)
