from dvd import DigitalVideoDisc


class Cart:
    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        self.items.append(dvd)

    def total_cost(self):
        return sum(dvd.cost for dvd in self.items)