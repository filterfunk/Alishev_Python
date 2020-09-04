a = ["first", 1, 2, 3, "second", 10, 20, "third", 15, 56, 70, "fourth", -50]

# print(a)
#

my_dict = {}
current_str = None

for e in a:
    if type(e) == str:
        my_dict[e] = []
        current_str = e
    else:
        my_dict[current_str].append(e)

print(my_dict)
