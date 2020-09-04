a = [1, 2, 3, 4, 5]

# Умножить каждый элемент списка на 2
# Вариант 1

b = []
for num in a:
    b.append(num * 2)
print(b)

# Вариант 2 - генератор списков

c = [num * 2 for num in a]
print(c)
