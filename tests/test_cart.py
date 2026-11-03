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


if __name__ == "__main__":
    unittest.main()
