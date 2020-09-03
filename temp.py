my_list = [7, 5, 4, 3, 2, 1, -5, -10, -13, -15, -18]

total2 = 0
for element in my_list:
    if element < 0:
        total2 += element

print(total2)
