import requests
from bs4 import BeautifulSoup
import csv

def getStats(link):
    playerInfo = []
    headers = {
        "User-Agent": "ExampleWikiScraper/1.0 (https://githhub.com/emcombs23; emcombs.23.sv@gmail.com)",
    }

    page = requests.get(link, headers = headers).text
    soup = BeautifulSoup(page, 'html.parser')

    headersSection = soup.find_all('thead', attrs = {'class': 'sidearm-primary'})
    print(len(headersSection))
    colHeaders = []
    rows = headersSection[1].find_all('tr')
    row = rows[0]
    cols = row.find_all('th')
    for th in cols[:3]:
        print(th.text.strip())
        colHeaders.append(th.text.strip())
    myRow = rows[1]

    cols = myRow.find_all('th')
    for th in cols:
        print(th.text.strip())
        colHeaders.append(th.text.strip())

    allStats = []
    tbodys = soup.find_all('tbody')
    tbody = tbodys[1]
    rows = tbody.find_all('tr')
    for row in rows[:-1]:
        allStats.append([])
        tds = row.find_all('td')
        for data in tds[:1]:
            #print(data.text.strip())
            allStats[-1].append(data.text.strip())

        span = tds[1].find('span')
        #print(span.text.strip())
        allStats[-1].append(span.text.strip())

        for data in tds[2:-1]:
            #print(data.text.strip())
            allStats[-1].append(data.text.strip())

    return colHeaders, allStats

getStats('https://hurstathletics.com/sports/mens-ice-hockey/stats/2025-26')

colHeaders, allStats = getStats('https://hurstathletics.com/sports/mens-ice-hockey/stats/2025-26')

print(allStats)



# ---- Write CSV ----
with open("hurst_hockey_Stats.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(colHeaders)
    writer.writerows(allStats)

print("CSV file created successfully!")
