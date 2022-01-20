# Task about 9-floor house
ap_num = int(input('Enter any apartment number: '))

floor = int

# 1st entrance
if 1 <= ap_num <= 36:
    floor = (ap_num + 3) // 4
    print('Apartment №', ap_num, 'is located on the', floor, "floor of the 1st entrance")
# 2nd entrance
elif 37 <= ap_num <= 72:
    floor = (ap_num - 36 + 3) // 4
    print('Apartment №', ap_num, 'is located on the', floor, "floor of the 2nd entrance")
# 3rd entrance
elif 73 <= ap_num <= 108:
    floor = (ap_num - 72+ 3) // 4
    print('Apartment №', ap_num, 'is located on the', floor, "floor of the 3rd entrance")
# 4th entrance
elif 109 <= ap_num <= 144:
    floor = (ap_num - 108 + 3) // 4
    print('Apartment №', ap_num, 'is located on the', floor, "floor of the 4th entrance")
# Non-existent apartment
else:
    print('This apartment (', ap_num, ') does not exist')
