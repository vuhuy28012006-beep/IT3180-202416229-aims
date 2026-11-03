from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title

dvds = [
    DigitalVideoDisc("The Lion King", 20.00),
    DigitalVideoDisc("Aladdin", 15.00),
    DigitalVideoDisc("Finding Nemo", 18.00)
]

result = search_by_title(dvds, "lion")

for dvd in result:
    print(dvd.title)