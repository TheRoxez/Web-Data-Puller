import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook

# URL'yi ve sayfadaki tablo sınıfını tanımlayın
url = "http://odtuteknokent.com.tr/tr/firmalar/tum-firmalar"
table_class = "table table-striped table-bordered"

# Web sayfasından verileri çekin
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("table", {"class": table_class})

# Verileri bir veri çerçevesinde depolayın
rows = []
if table is not None:
    for row in table.find_all("tr"):
        cells = row.find_all("td")
        if cells:
            name = cells[0].text.strip()
            sector = cells[1].text.strip()
            rows.append([name, sector])

df = pd.DataFrame(rows, columns=["Şirket", "Link"])

# Verileri Excel dosyasına yazdırın
dosya = 'Şirketler.xlsx'
book = Workbook()
sheet = book.active

for row in df.iterrows():
    row_values = list(row[1].values)
    sheet.append(row_values)

book.save(dosya)