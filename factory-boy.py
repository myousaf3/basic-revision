'''
Implement flow of a factory pattern for the creation of a car,
in which there are different objects like seats, engine, doors, multimedia, suspension, electrical system etc. 
Ensuring only a single object of the Car Factory is ever available, 
keep track of cars produced by the factory and provide an interface to get a list of all those cars and their counts. 
Factory should help make a car with custom requirements for all mentioned components, with sensible defaults set.
'''


class Car:
    def __init__(self, seats, engine, doors, multimedia, suspension, electrical_system):
        self.seats = seats
        self.engine = engine
        self.doors = doors
        self.multimedia = multimedia
        self.suspension = suspension
        self.electrical_system = electrical_system


class CarFactory:
    def __init__(self):
        self.cars = []

    def create_car(self, seats=4, engine='1000cc', doors=4, multimedia=True, suspension="Soft", electrical_system="Electrical"):
        car = Car(seats=seats, engine=engine, doors=doors, multimedia=multimedia,
                suspension=suspension, electrical_system=electrical_system)
        self.cars.append(car)
        return self.cars

    def get_count(self):
        return self.cars

    def car_details(self):
        return (self.cars)


if __name__ == "__main__":
    print("_________________Welcome to Car Factory_________________")
    factory = CarFactory()
    car1 = factory.create_car(4, "2000cc", 2, True, "Hard", "Efficient")
    car2 = factory.create_car(2, "4000cc", 4, True, "Soft", "Nice")
    cars_made = len(factory.get_count())
    print("All cars made from factory: ", cars_made)
    cars_details = factory.car_details()
    print("All cars details: ")
    for i in range(cars_made):
        print(f"Car", i, "Engine:", cars_details[i].engine, "Seats:",
            cars_details[i].seats, "Doors:", cars_details[i].doors)
