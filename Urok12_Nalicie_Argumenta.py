# Передаём в функцию множество и список, если все элементы списка есть в множестве - True

input_set = {1, 2, 10, 4, 5, 'hello'}
input_list = [1]

def my_func(input_set, input_list):
    for el in input_list:
        if el not in input_set:
            return False

        return True


print(my_func(input_set, input_list))


#input_list = set(input_list)


# def my_func(input_set, input_list):
#   print(input_list in input_set)


# my_func(input_set, input_list)