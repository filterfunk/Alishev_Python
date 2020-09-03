n = int(input("Введите исходное число: "))
k = int(input("В какую степень будем возводить: "))

a = list(range(1, n))


def funk1(n, k):
    if n > 20:
        return 0
    else:
        number_sum = 0
        for i in a:
            if i % 2 == 0:  # Находим чётные числа
                number_sum += i ** k  # Возводим в степень К каждое чётное число
                # number_sum += i  # Прибавляем к number_sum результат возведения в степень
    print(number_sum)


funk1(n, k)
