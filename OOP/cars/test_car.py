from car import ElectricCar

def test_ElectricCar_init:

    ec = ElectricCar(100)
    assert ec._ElectriCar__max_range == 100

def charge(self):
    self.counter = 0
