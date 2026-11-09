class Instrument:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def play(self):
        return f"Играет"

    def get_info(self):
        return f"{self.name} стоит {self.price} рублей"

class Guitar(Instrument):
    def __init__(self, name, price, strings):
        super().__init__(name, price)
        self.strings = strings

    def play(self):
        return "Бренчит на гитаре"

    def tune(self):
        return "Настраивает струны"

class Piano(Instrument):
    def __init__(self, name, price, keys):
        super().__init__(name, price)
        self.keys = keys

    def play(self):
        return "Играет на пианино"

    def open_lid(self):
        return "Открывает крышку"

class Drum(Instrument):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = ["маленький", "средний", "большой"]

    def play(self):
        return "Бьет барабан"

    def hit_hard(self):
        return "Сильно ударяет по барабану"

#создание объектов
guitar = Guitar("Yamaha F310", "30 000", "6")
piano = Piano("Concert 8", "3 000 000", "88")
drum = Drum("Roland VAD716SW", "1 200 000", "большой")

#иинформация об инструментах
instruments = [guitar, piano, drum]
for instrument in instruments:
    print(f"{instrument.get_info()}")

#переопределенные метолы от родительского класса
for instrument in instruments:
    print(f"{instrument.play()}")

#уникальные методы дечерних классов
print(f"{guitar.tune()}")
print(f"{piano.open_lid()}")
print(f"{drum.hit_hard()}")
