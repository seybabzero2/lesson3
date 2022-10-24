# class Human:
#     def __init__(self, name = "Human"):
#         self.name = name
# class Auto:
#     def __init__(self, brand):
#         self.brand = brand
#         self.passengers = []
#     def add_passenger(self, *args):
#         for passengers in args:
#             self.passengers.append(passengers)
#     def print_passangers_names(self):
#         if self.passengers != []:
#             print(f"{self.brand} has passengers: ")
#             for passengers in self.passengers:
#                 print(passengers.name)
#         else:
#             print("Car is empty")
#
# nick = Human("Anatolii")
# kate = Human("Nastya")
# car = Auto("BMW")
# car.add_passenger(nick, kate)
# car.print_passangers_names()

import random

class Human:
    def __init__(self, name="Human", job = None, home = None, car = None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
    def get_home(self):
        self.home = House()
    def get_car(self):
        self.car = Auto(brands_of_car)
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)
    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5
    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4
    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
            if manage == "fuel":
                print("I bought fuel")
                self.money -= 100
                self.car.fuel += 100
            elif manage == "food":
                print("Bought food")
                self.money -= 50
                self.home.food +=50
