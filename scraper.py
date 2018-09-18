from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
pageToScrape = 'https://www.utdallas.edu/shop/parking/_code.php'
page = urlopen(Request(pageToScrape, headers={'User-Agent': 'Mozilla'}))
soup = BeautifulSoup(page, 'html.parser')
h1 = soup.find('table', attrs={'summary':'Parking Structure 4'})
h1Text = h1.tbody # this will contain each entry in the table for a single parking structure
x = 0
for child in h1Text:
    if hasattr(child,'attrs'):
        numSpace = str(child.td.next_sibling.next_sibling.next_sibling.next_sibling.contents[0])
        if numSpace[0] == '<':
            print(0)
        else:
            print(numSpace)