import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url_format = "https://books.toscrape.com/catalogue/page-{}.html"
data = []

for p in range(1, 4):
    req = requests.get(url_format.format(p))
    if req.status_code != 200:
        break
        
    soup = BeautifulSoup(req.content, 'html.parser')
    items = soup.find_all('article', class_='product_pod')
    
    for item in items:
        titre = item.h3.a['title']
        prix = item.find('p', class_='price_color').text.replace('Â', '').strip()
        dispo = item.find('p', class_='availability').text.strip()
        
        data.append({
            'Titre': titre,
            'Prix': prix,
            'Disponibilité': dispo
        })
        
    time.sleep(1)

df = pd.DataFrame(data)
df.to_excel('liste_livres_pages_1_a_3.xlsx', index=False)
print("Extraction terminée : 60 lignes sauvegardées.")
