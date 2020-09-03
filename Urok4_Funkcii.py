name = int(input('Введи имя'))
height = int(input('Введи рост в сантиметрах'))
weight = int(input('Введи вес'))

height = float(height)/100

def bmi_calc(name, height, weight):
    bmi = float(weight) / (float(height) ** 2)

    print('У ' + name + ' ИМТ = ' + str(bmi))
    if bmi < 25:
        print('Всё нормально с весом')
    if bmi > 25:
        print('Надо худеть')


bmi_calc(name, height, weight)
