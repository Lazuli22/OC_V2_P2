import requests
import argparse
from bs4 import BeautifulSoup
from un_livre import (
    imprimer_infos_livre, collecter_infos_livre
)
from livres_une_categorie import (
    collecter_livres_categorie, collecter_pages_categorie
)


def collecter_tout_site(url_site):
    """ scrappe the web site """
    nbre_livres_site = 0
    nom_cat = ""
    url_cat = ""
    liste_livres = []
    response = requests.get(url_site)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        for i in range(1, 51):
            nom_cat = soup.select_one(f"#default>div>div>div>aside>div.side_categories>ul>li>ul>li:nth-child({i})>a")
            nom_categorie = nom_cat.text.strip(" \n ").rstrip(" \n ")
            print(nom_categorie)
            url_cat = soup.select_one(f"#default>div>div>div>aside>div.side_categories>ul>li>ul>li:nth-child({i})>a")
            url_categorie = "http://books.toscrape.com/"+url_cat["href"]
            print(url_categorie)
            liste_livres = collecter_livres_categorie(collecter_pages_categorie(url_categorie))
            imprimer_infos_livre(liste_livres, nom_categorie)
            nbre_livres_site += len(liste_livres)
    print("nombre total de livres \n :" + str(nbre_livres_site))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-scrap', "-s",  dest='portee', required=True,
                        choices=['book', 'categorie', 'site'],
                        help="Choisissez la portée du Scrapping. Souhaitez vous scrapper \
                        les informations d'un livre ou  \
                        les livres d'une catégorie ou  \
                        Le site dans sa globalité")
    parser.add_argument('-url', '-u',  help="Préciser l'url à Scrapper")
    args = parser.parse_args()
    port = args.portee
    url_port = args.url
    if port == 'book':
        imprimer_infos_livre([collecter_infos_livre(url_port)], "monlivre")
    elif port == 'categorie':
        imprimer_infos_livre(collecter_livres_categorie(collecter_pages_categorie(url_port)), "des_livres")
    elif port == 'site':
        collecter_tout_site(url_port)
    else:
        print("Vous n'avez pas choisi d'option correct, veuillez relancer le programme")


if __name__ == "__main__":
    main()
