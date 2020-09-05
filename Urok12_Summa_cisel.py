# Найти сумму уникальных чисел

my_list = [1, 1, 2, 5, 10, 10, 10]

my_set = set(my_list)

summa = 0
for e in my_set:
    summa = summa + e
print(summa)


#Решение с помощью функции sum
print(sum(set(my_list)))
