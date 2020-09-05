class Person():
    # Инициализация атрибутов класса
    def __init__(self, name, surname, place):
        self.name = name
        self.surname = surname
        self.place = place
        print("Создан экземпляр класса Person")

    # Инициализация методов класса
    def birth(self):
        print(self.name.title() + ' родился')


# Создание экземпляров класса
p1 = Person("Петя", "Иванов")
print(p1.name)

# Вызов метода
p1.birth()

# p1 = Person(name, surname, place)
# p1.name = "Elon"
# p1.surname = "Mask"
# p1.place = "UAR"
#
# p1 = Person()
# p1.name = "Иван"
# p1.surname = "Петров"
# p1.place = "СССР"
