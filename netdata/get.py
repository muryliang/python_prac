import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html, "html.parser")
table = bsObj.findAll("table", {"class":"wikitable"})[0]
rows = table.findAll("tr")

csvFile = open("editors.csv", 'wt', newline="\n", encoding='utf-8')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']): #findAll can pass a list as source
            print (cell.get_text())
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()
