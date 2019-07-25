from class1 import Car

if __name__ == "__main__":
    car_1 = Car("KA013060",4)
    car_2 = Car("KA013060",5)
    car_3 = Car("KA013060",6)
    car_4 = Car("KA013060",4)
    car_5 = Car("KA013060",4)
    car_1.start()
    car_2.start()
    car_3.start()
    car_1.change_gear()
    car_2.change_gear()
    car_3.change_gear()
    car_2.change_gear()
    car_4.change_gear()

    lst = [car_1,car_2,car_3,car_4,car_5]

    for car in lst:
        car.showInfo()
    c = len(list(filter(lambda x:x.is_started and x.c_gear)))
    print(c)
