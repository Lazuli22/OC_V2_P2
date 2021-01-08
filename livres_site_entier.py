import requests
from bs4 import BeautifulSoup
from math import *
from un_livre import infos_book, imprime_infos
from livres_une_categorie import livres_categorie


def livres_tout_site(url):
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        for i in range(1, 51):
            nom_categorie = soup.select_one("#default > div > div > div > aside > div.side_categories > ul > li > ul > li:nth-child("+str(i)+") > a").text.strip(" \n ").rstrip(" \n ")
            print(nom_categorie)
            url_categorie = "http://books.toscrape.com/"+soup.select_one("#default > div > div > div > aside > div.side_categories > ul > li > ul > li:nth-child("+str(i)+") > a")["href"]
            print(url_categorie)
            imprime_infos(livres_categorie(url_categorie), nom_categorie)


livres_tout_site("http://books.toscrape.com/index.html")