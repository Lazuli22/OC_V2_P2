import requests
from math import ceil
from bs4 import BeautifulSoup
from un_livre import (
    collecter_infos_livre, telecharger_image, DIR_IMAGES
)


def collecter_pages_categorie(url_categorie):
    """return a list of page url of a category """
    liste_pages_categorie = []
    response = requests.get(url_categorie)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        nbre_livres = soup.select_one("#default>div>div>div>div>form>strong:nth-child(2)").text
        nbre_pages = ceil(int(nbre_livres)/20)
        liste_pages_categorie = [url_categorie if i == 1 else
                                 url_categorie.replace("index.html", f"page-{i}.html") for i in range(1, nbre_pages+1)]
    return liste_pages_categorie


def collecter_livres_categorie(liste_pages_categorie):
    """ return a list of books by category """
    liste_livres = []
    infos_livre = ""
    url_livre = ""
    for une_url in liste_pages_categorie:
        response = requests.get(une_url)
        response.encoding = "utf8"
        if response.ok:
            soup = BeautifulSoup(response.text, "html.parser")
            liste_articles = soup.findAll("article")
            for i in range(1, len(liste_articles)+1):
                urlr = soup.select_one(f"#default>div>div>div>div>section>div:nth-child(2)> \
                ol>li:nth-child({i})>article>h3>a")['href'].strip("../../../")
                url_livre = "http://books.toscrape.com/catalogue/" + urlr
                infos_livre = collecter_infos_livre(url_livre)
                telecharger_image(infos_livre['image_url'], infos_livre['universal_ product_code'])
                infos_livre["image_url"] = DIR_IMAGES + "/" + infos_livre['universal_ product_code']+".jpeg"
                liste_livres.append(infos_livre)
    return liste_livres
