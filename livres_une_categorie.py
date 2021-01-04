import requests
from bs4 import BeautifulSoup

from un_livre import infos_book, imprime_infos


def livres_categorie(url):
    liste_livres = []
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        liste_articles = soup.findAll("article")
        for i in range(1, len(liste_articles)+1):
            url_livre = "http://books.toscrape.com/catalogue/" + soup.select_one("#default > div > div > div > div > section > div:nth-child(2) > ol > li:nth-child("+str(i)+") > article > h3 > a")['href'].strip("../../../")
            #print("-----------------")
            #print(url_livre)
            #print("\n")
            #print(infos_book(url_livre))
            liste_livres.append(infos_book(url_livre))
    print(len(liste_livres))
    return liste_livres


imprime_infos(livres_categorie("http://books.toscrape.com/catalogue/category/books/travel_2/index.html"), 'des_livres')