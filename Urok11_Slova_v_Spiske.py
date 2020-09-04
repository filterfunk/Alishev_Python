# Каждому слову с длиной >5 , добавить точку на конце

words = ['hello', 'hey', 'goodbye', 'guitar', 'piano']

c = [word + '.' for word in words if len(word) > 5]
print(c)


words.append('33')
print(words)
