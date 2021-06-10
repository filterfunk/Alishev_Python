x = input('Введи количество миль\n')


def convertor(x):
    y = float(x) * 1.609
    print('В ' + x + ' милях - ' + str(y) + ' километров')


convertor(x)
