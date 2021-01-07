import requests
from bs4 import BeautifulSoup
from math import *
from un_livre import infos_book, imprime_infos

# retour la liste des livres d'une catégorie - A ameliorer 
def livres_categorie(url):
    nbre_livres = 0
    liste_livres = []
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        nbre_livres = soup.select_one("#default > div > div > div > div > form > strong:nth-child(2)").text
        nbre_pages = ceil(int(nbre_livres)/20)
        #print(nbre_pages)
        liste_articles = soup.findAll("article")
        for i in range(1, len(liste_articles)+1):
            url_livre = "http://books.toscrape.com/catalogue/" + soup.select_one("#default > div > div > div > div > section > div:nth-child(2) > ol > li:nth-child("+str(i)+") > article > h3 > a")['href'].strip("../../../")
            liste_livres.append(infos_book(url_livre))
        if nbre_pages > 1:
            for i in range(2, nbre_pages+1):
                nurl = url.replace("index.html", "page-"+str(i)+".html")
                res = requests.get(nurl)
                soup2 = BeautifulSoup(res.text, "html.parser")
                liste_articles = soup2.findAll("article")
                for i in range(1, len(liste_articles)+1):
                    url_livre = "http://books.toscrape.com/catalogue/" + soup2.select_one("#default > div > div > div > div > section > div:nth-child(2) > ol > li:nth-child("+str(i)+") > article > h3 > a")['href'].strip("../../../")
                    liste_livres.append(infos_book(url_livre))
    return liste_livres


livres_categorie("http://books.toscrape.com/catalogue/category/books/travel_2/index.html")
#imprime_infos(livres_categorie("http://books.toscrape.com/catalogue/category/books/classics_6/index.html"), 'des_livres')