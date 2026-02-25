import requests
from bs4 import BeautifulSoup
import csv

def getPlayerInfo(link):
    playerInfo = []
    headers = {
        "User-Agent": "ExampleWikiScraper/1.0 (https://githhub.com/emcombs23; emcombs.23.sv@gmail.com)",
    }

    page = requests.get(link, headers = headers).text
    soup = BeautifulSoup(page, 'html.parser')


    divTag = soup.find('div', attrs = {'class': 'sidearm-roster-player-header-info'})
    #print(divTag)

    nameTags = divTag.find('span', attrs = {'class': 'sidearm-roster-player-name'})
    names = nameTags.find_all('span')
    for name in names:
        print(name.text)
        playerInfo.append(name.text.strip())

    numTag = divTag.find('span', attrs = {'class': 'sidearm-roster-player-jersey-number'})
    print(numTag.text.strip())
    playerInfo.append(numTag.text.strip())

    bioSection = divTag.find('div', attrs = {'class': 'sidearm-roster-player-fields flex flex-item-1'})

    #print(bioSection)

    bioTags = bioSection.find_all('li', attrs = {'class': 'large-6 flex columns'})
    for bio in bioTags:
        info = bio.find('dd')
        print(info.text.strip())
        playerInfo.append(info.text.strip())
    print('------------------')
    return playerInfo

    

headers = {
        "User-Agent": "ExampleWikiScraper/1.0 (https://githhub.com/emcombs23; emcombs.23.sv@gmail.com)",
    }

page = requests.get('https://hurstathletics.com/sports/mens-ice-hockey/roster/henry-hunt/17628', headers = headers).text
soup = BeautifulSoup(page, 'html.parser')

players = soup.find_all('li', attrs = {'class': 'sidearm-roster-player-list-item flex flex-align-center'})
print(len(players))


links = []
for player in players:
    nameTag = player.find('div', attrs = {'class': 'sidearm-roster-player-list-item-name'})
    link = nameTag.find('a')['href']
    url = 'https://hurstathletics.com' + link
    links.append(url)
    #print(url)


for link in links:
    getPlayerInfo(link)




all_players = []

for link in links:
    data = getPlayerInfo(link)
    if data:
        all_players.append(data)

print(all_players)

headers = ["FirstName", "LastName", "JerseyNumber", "Position", "Height", "Weight", "AcademicYear", "Hometown", "Highschool"]


# ---- Write CSV ----
with open("hurst_hockey_roster.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(all_players)

print("CSV file created successfully!")



