a = int(input('Введи число'))

def chetnost(a):
    c = int(a) % 2

    print('Остаток от деления на 2 = ' + str(c))
    if c == 0:
        print('Число ' + str(a) + ' чётное')
    if c != 0:
        print('Число ' + str(a) + ' нечётное')


chetnost(a)
