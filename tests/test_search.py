import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class SearchByTitleTests(unittest.TestCase):
    def test_search_is_case_insensitive(self):
        dvd = DigitalVideoDisc("The Lion King", 20.0)
        self.assertEqual(search_by_title([dvd], "lion"), [dvd])

    def test_search_uses_unicode_case_folding(self):
        dvd = DigitalVideoDisc("Straße", 20.0)
        self.assertEqual(search_by_title([dvd], "STRASSE"), [dvd])


if __name__ == "__main__":
    unittest.main()
