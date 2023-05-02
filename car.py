class Car:
    def __init__(self, kilometers = 0, last_maintenance = 0):

        self.kilometers = kilometers
        self.last_maintenance = last_maintenance

    def repair(self):

        print('Car is being repaired')
        self.last_maintenance = self.kilometers

    def drive(self, distance):

        self.kilometers += distance
        print(f"Driving: {distance}")
        if self.kilometers - self.last_maintenance >= 30000:
            print('You need to maintain your car!')
            self.repair()

    def __str__(self):
        return f"This car has driven {self.kilometers} kilometers"
    

auto = Car()
auto.drive(20000)
auto.drive(10)
auto.drive(30)
auto.drive(2030303030)
auto.drive(2020)
auto.drive(1988)
auto.drive(2000000000000000000000)
auto.drive(2020)
auto.drive(100)
auto.kilometers


