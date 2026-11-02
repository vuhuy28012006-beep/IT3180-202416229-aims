
from aims.dvd import DigitalVideoDisc


class Cart:
    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        self.items.append(dvd)

    def total_cost(self):
        return sum(dvd.cost for dvd in self.items)

    def print_cart(self):
        # Kiểm tra giỏ hàng có DVD hay không
        if not self.items:
            print("The cart is empty")
            return

        # Hiển thị danh sách DVD
        print("Cart contents:")

        for index, dvd in enumerate(self.items, start=1):
            print(f"{index}. Title: {dvd.title}, Cost: {dvd.cost:.2f} $")

        # Hiển thị tổng tiền
        print(f"Total cost: {self.total_cost():.2f} $")
