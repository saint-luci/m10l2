from threading import Thread
from time import sleep

class Knight(Thread):
    name = ""
    power = 0

    def __init__(self, name, power):
        self.name = name
        self.power = power
        super().__init__()

    def run(self):
        print(f"{self.name}, на нас напали!")
        count_of_days = 0
        count_of_wariors = 100
        while count_of_wariors > 0:
            count_of_wariors -= self.power
            count_of_days += 1
            sleep(1)
            print(f"{self.name} сражается {count_of_days}, осталось {count_of_wariors} врагов!")
        print(f"{self.name} одержал победу спустя {count_of_days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print("Все битвы закончились!")
