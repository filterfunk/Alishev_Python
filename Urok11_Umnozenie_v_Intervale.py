# В интервале от 10 до 1 отфильтровать чётные числа и умножить каждое на 2

c = [num * 2 for num in range(10, 1, -1) if num % 2 == 0]
print(c)
