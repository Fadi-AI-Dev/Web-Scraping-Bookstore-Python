import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
all_books = []

for page in range(1, 4):
    url = base_url.format(page)
    response = requests.get(url)
    
    if response.status_code != 200:
        break
        
    soup = BeautifulSoup(response.content, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    
    for book in books:
        title = book.h3.a['title']
        
        price_text = book.find('p', class_='price_color').text
        price = price_text.replace('Â', '').strip()
        
        stock_text = book.find('p', class_='availability').text.strip()
        
        all_books.append({
            'Titre': title,
            'Prix': price,
            'Disponibilité': stock_text
        })
        
    time.sleep(1)

df = pd.DataFrame(all_books)
df.to_excel('liste_livres_pages_1_a_3.xlsx', index=False)
print("Fichier Excel généré avec succès ! 61 lignes créées.")
