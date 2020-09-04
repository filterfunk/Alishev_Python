arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12]]


def print_2d(arr):
    for i in arr:

        k = i[::-1]

        for j in k:
            print(j, end=' ')

        print()


print_2d(arr)
