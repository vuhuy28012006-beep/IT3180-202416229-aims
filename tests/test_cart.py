import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class CartLimitTests(unittest.TestCase):
    def test_cart_rejects_the_21st_dvd(self):
        cart = Cart()
        for number in range(20):
            cart.add_dvd(DigitalVideoDisc(f"DVD {number + 1}", 1.0))

        accepted = cart.add_dvd(DigitalVideoDisc("DVD 21", 1.0))

        self.assertFalse(accepted)
        self.assertEqual(len(cart.items), 20)

    def test_cart_accepts_exactly_20_dvds(self):
        cart = Cart()
        for number in range(20):
            accepted = cart.add_dvd(DigitalVideoDisc(f"DVD {number + 1}", 1.0))
            self.assertTrue(accepted)

        self.assertEqual(len(cart.items), 20)

    def test_empty_cart_total_cost_is_zero(self):
        self.assertEqual(Cart().total_cost(), 0)

    def test_total_cost_sums_all_dvds(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD A", 10.50))
        cart.add_dvd(DigitalVideoDisc("DVD B", 4.25))

        self.assertAlmostEqual(cart.total_cost(), 14.75)
    def test_sort_by_title(self):
        cart = Cart()

        cart.add_dvd(DigitalVideoDisc("Spider-Man", 20.0))
        cart.add_dvd(DigitalVideoDisc("Avatar", 15.0))
        cart.add_dvd(DigitalVideoDisc("Harry Potter", 10.0))

        cart.sort_by_title()

        titles = [dvd.title for dvd in cart.items]

        self.assertEqual(
            titles,
            ["Avatar", "Harry Potter", "Spider-Man"]
        )

    def test_sort_by_cost(self):
        cart = Cart()

        cart.add_dvd(DigitalVideoDisc("DVD A", 20.0))
        cart.add_dvd(DigitalVideoDisc("DVD B", 10.0))
        cart.add_dvd(DigitalVideoDisc("DVD C", 15.0))

        cart.sort_by_cost()

        costs = [dvd.cost for dvd in cart.items]

        self.assertEqual(costs, [10.0, 15.0, 20.0])


if __name__ == "__main__":
    unittest.main()
