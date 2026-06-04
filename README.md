# 🕸️ Web Scraping Bookstore - Python & BeautifulSoup

Ce projet est un script d'automatisation en Python conçu pour extraire de manière structurée les données d'un site e-commerce de livres sur plusieurs pages. Les informations collectées sont nettoyées puis exportées directement dans un fichier Excel exploitable.

## 📊 Fonctionnalités
* **Navigation multi-pages :** Gestion automatique de la pagination (exploration séquentielle des pages).
* **Extraction ciblée :** Récupération dynamique des titres complets, des prix et de l'état des stocks.
* **Nettoyage de données :** Suppression automatique des artefacts de texte et encodages indésirables (ex: symboles résiduels).
* **Export structuré :** Génération automatique d'un fichier Excel (`.xlsx`) via la bibliothèque Pandas.

## 🛠️ Technologies & Bibliothèques utilisées
* **Python 3**
* **Requests :** Pour l'envoi des requêtes HTTP et la récupération du code HTML source.
* **BeautifulSoup4 :** Pour le parsing et l'extraction des éléments du DOM HTML.
* **Pandas :** Pour la structuration des données en DataFrame et l'export e-commerce.
* **Openpyxl :** Moteur d'écriture requis pour la génération des fichiers Excel.

## 🚀 Comment lancer le projet

1. **Cloner le projet ou télécharger le script :**
```bash
   git clone https://github.com/Fadi-Al-Dev/Web-Scraping-Bookstore-Python.git
```
