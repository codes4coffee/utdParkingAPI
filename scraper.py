from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json
pageToScrape = 'https://www.utdallas.edu/shop/parking/_code.php'
page = urlopen(Request(pageToScrape, headers={'User-Agent': 'Mozilla'}))
soup = BeautifulSoup(page, 'html.parser')
parkingStructures = ['Parking Structure 1', 'Parking Structure 3', 'Parking Structure 4']
parkingStructuresShort = ['PS1', 'PS3', 'PS4']
finalList = []
index = 0
#List the amount of spots for every parking structure 1 - 4
for structure in parkingStructures:
    jsonObj = {'structure': structure}
    jsonObj[shortName] = parkingStructuresShort[index]
    index += 1
    print(structure)
    parkingTable = soup.find('table', attrs={'summary':structure})
    tableData = parkingTable.tbody # this will contain each entry in the table for a single parking structure
    for child in tableData:
        if hasattr(child,'attrs'):

            color = str(child.td.next_sibling.next_sibling)[11:] #Get the permit type of the space and strip out the type from the html tag
            color = color[:color.find('"')]
            print(color)

            numSpace = str(child.td.next_sibling.next_sibling.next_sibling.next_sibling.contents[0])
            if numSpace[0] == '<':
                print(0)
                jsonObj[color] = 0
            else:
                print(numSpace)
                jsonObj[color] = int(numSpace)
    finalList.append(jsonObj)
    print(json.dumps(jsonObj))
    print('\n')

print(json.dumps(finalList))
