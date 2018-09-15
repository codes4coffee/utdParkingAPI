from urllib.request import urlopen
from bs4 import BeautifulSoup
pageToScrape = 'https://www.utdallas.edu/shop/parking/_code.php'
page = urlopen(pageToScrape)
soup = BeautifulSoup(page, 'html.parser')
h1 = soup.find('table', attrs={'summary':'Parking Structure 4'})
h1Text = h1.tbody # this will contain each entry in the table for a single parking structure
#print(h1Text.contents)
#print('hello')
x = 0
for child in h1Text:
    if hasattr(child,'attrs'):
        print(child.td.next_sibling.next_sibling.next_sibling.next_sibling.contents)