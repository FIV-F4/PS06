import requests
from bs4 import BeautifulSoup
import csv

url = "https://"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

rows = soup.find_all("tr")
data = []
for row in rows:
    cols = row.find_all("td")
    clean_cols = [col.text.strip() for col in cols]
    data.append(clean_cols)

print(data)