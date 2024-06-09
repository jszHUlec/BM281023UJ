class Car:
    def __init__(self, color, window_number, price): #konstruktor
        self.color = color
        self.window_number =window_number
        self.price = price

    def wyswietl(self):
        print(self.color, self.window_number, self.price, "****")


car1 = Car("czerwony", 2, 300)
car2 = Car("niebieski", 4, 600)

print(car1.color)
print(car2.color)
print(car1.wyswietl())
print(car2.wyswietl())



