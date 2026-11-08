class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.battery = 100
        self.is_on = False
        pass

    def turn_on(self):
        if self.is_on:
            print("Телефон уже включен")
        elif not self.is_on and self.battery == 0:
            print(f"Телефон разряжен")
        else:
            self.is_on = True
            pass


    def turn_off(self):
        self.is_on = False
        pass

    def make_call(self, duration):
        if duration <= 0:
            print("Некорректная продолжительность звонка")
            return
        if not self.is_on:
            print(f"Телефон выключен")
        elif self.is_on:
            consumption = duration * 2
            if self.battery >= consumption:
                self.battery -= consumption
            else:
                print("Недостаточно заряда")
        pass

    def charge(self, amount):
        if amount <= 0:
            print("Некорректное значение зарядки")
            return
        elif self.battery + amount > 100:
            self.battery = 100
            print("Телефон полностью заряжен")
        else:
            self.battery += amount
        pass

    def get_status(self):
        if self.battery > 50:
            battery_icon = "🔋"
        elif self.battery > 20:
            battery_icon = "🪫"
        else:
            battery_icon = "⚠️"

        status = f"Включен" if self.is_on else "Выключен"

        return {
            "brand": self.brand,
            "model": self.model,
            "battery": self.battery,
            "is_on": status,
            "smile_status": battery_icon
        }


iphone = Phone("Apple", "Iphone 15 Pro")
samsung = Phone("Samsung", "Galaxy S24")
xiaomi = Phone("Xiaomi", "Redmi Note 13")

iphone.turn_on()
iphone.make_call(15)
iphone.make_call(20)
iphone.charge(50)
iphone.get_status()


samsung.turn_on()
samsung.make_call(15)
samsung.make_call(20)
samsung.make_call(20)
samsung.charge(1)
samsung.get_status()


xiaomi.turn_on()
xiaomi.make_call(5)
xiaomi.make_call(7)
xiaomi.charge(10)
xiaomi.get_status()


# звонок с выключенного телефона
xiaomi.turn_off()
xiaomi.make_call(15)
#Телефон выключен

# попытка включить телефон с 0% батареи
samsung.turn_off()
samsung.battery = 0
samsung.turn_on()
#Телефон разряжен

# звонок, на который не хватает заряда
iphone.make_call(50)
#Недостаточно заряда

# зарядка выше 100%
iphone.charge(120)
#по моей логике он заряжается только до 100% и выдает об этом сообщение

iphone.charge(-20)
#получаю сообщение Некорректное значение зарядки

# отображение разных смайликов батареи
iphone.battery = 21
samsung.battery = 51
xiaomi.battery = 19

print(iphone.get_status()["smile_status"])
print(samsung.get_status()["smile_status"])
print(xiaomi.get_status()["smile_status"])
