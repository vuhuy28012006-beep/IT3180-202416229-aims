from aims.dvd import DigitalVideoDisc
from aims.cart import Cart

cart = Cart()
cart.add_dvd(DigitalVideoDisc("DVD 1", 20.00))
cart.add_dvd(DigitalVideoDisc("DVD 2", 43.89))

print(f"Total cost: {cart.total_cost():.2f} $")