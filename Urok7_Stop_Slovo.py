words = ["apple", "banana", "grape", "other", "stop", "hello", "goodbye"]

# Выйти из цикла при слове stop

# for
for element in words:
    if element == "stop":
        break
    else:
        print(element)
# while
i1 = 0
while words[i1] != "stop":
    print(words[i1])

    i1 += 1
