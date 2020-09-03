my_list = [7, 5, 4, 3, 2, 1, -5, -10, -13, -15, -18]

# Найти сумму отрицательных чисел

# Решение с while

total1 = 0
i1 = -1

while my_list[i1] < 0:
    total1 += my_list[i1]
    i1 -= 1

print(total1)


# Решение с for

my_list = [7, 5, 4, 3, 2, 1, -5, -10, -13, -15, -18]

total2 = 0
for element in my_list:
    if element < 0:
        total2 += element

print(total2)
