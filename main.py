from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from flask import Response
import json
pageToScrape = 'https://www.utdallas.edu/shop/parking/_code.php'
page = urlopen(Request(pageToScrape, headers={'User-Agent': 'Mozilla'}))
soup = BeautifulSoup(page, 'html.parser')
parkingStructures = ['Parking Structure 1', 'Parking Structure 3', 'Parking Structure 4']

def getParkingSpaces(request):
    finalList = []
    #List the amount of spots for every parking structure 1 - 4
    for structure in parkingStructures:
        jsonObj = {'structure': structure}
        parkingTable = soup.find('table', attrs={'summary':structure})
        tableData = parkingTable.tbody # the sub-table for a single parking structure
        for child in tableData:
            if hasattr(child,'attrs'):

                color = str(child.td.next_sibling.next_sibling)[11:] #Get the permit type of the space and strip out the type from the html tag
                level = str(child.td)[19:]
                color = color[:color.find('"')]
                level = level[:level.find('<')]
                color = color + '-' + level

                numSpace = str(child.td.next_sibling.next_sibling.next_sibling.next_sibling.contents[0])
                if numSpace[0] == '<':
                    jsonObj[color] = 0
                else:
                    jsonObj[color] = int(numSpace)
        finalList.append(jsonObj)
        resp = Response(json.dumps(finalList), mimetype='application/json')
    return resp