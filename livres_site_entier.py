import requests
from bs4 import BeautifulSoup
from un_livre import (
    imprimer_infos_livre, collecter_infos_livre
)
from livres_une_categorie import (
    collecter_livres_categorie, collecter_pages_categorie
)


def collecter_tout_site(url_site):
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
    print("Que souhaitez-vous faire?")
    print("1 - imprimer dans un fichier CSV les informations d'un livre?")
    print("2 - imprimer tous les informations des livres associés à une catégorie ?")
    print("3 - imprimer tous les livres du site entier dans des fichier CSV différents ?\n\
    Chaque fichier CSV contiendra l'ensemble des informations des livres d'une categorie. \n \
    Dans le même temps l'image associée au livre sera téléchargé")
    choix = int(input())
    if(choix == 1):
        print("Veuillez préciser l'url du livre à imprimer:")
        url_un_libre = input()
        imprimer_infos_livre([collecter_infos_livre(url_un_libre)], "monlivre")
        print("les informations du livre sont dans monlivre.csv")
    elif(choix == 2):
        print("Veuillez préciser l'url d'une categorie à imprimer:")
        url_categorie = input()
        imprimer_infos_livre(collecter_livres_categorie(collecter_pages_categorie(url_categorie)), "des_livres")
        print("les informations de la catégorie demandée sont  dans des_livres.csv")
    elif(choix == 3):
        collecter_tout_site("http://books.toscrape.com/index.html")
    else:
        print("Vous n'avez pas choisi d'option correct, veuillez relancer le programme")


if __name__ == "__main__":
    main()
