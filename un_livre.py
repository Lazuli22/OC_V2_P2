import requests
import csv
import os
from bs4 import BeautifulSoup


DIR_FILES = "data"
DIR_IMAGES = "data/images"


def collecter_infos_livre(url):
    """ scrap informations of a book"""
    dict_infos_book = {}
    response = requests.get(url)
    response.encoding = "utf8"
    if response.ok:
        sp = BeautifulSoup(response.text, "html.parser")
        dict_infos_book['product_page_url'] = url
        upc = sp.select_one("#content_inner>article>table>tr:nth-child(1)>td").text
        dict_infos_book['universal_ product_code'] = upc
        title = sp.find('title').text.strip("\n ").rstrip("\n")
        dict_infos_book['title'] = title
        pit = sp.select_one("table>tr:nth-child(4)>td:nth-child(2)").text
        dict_infos_book['price_including_tax'] = pit
        pet = sp.select_one("#content_inner>article>table> tr:nth-child(3)>td").text
        dict_infos_book['price_excluding_tax'] = pet
        na = sp.select_one("#content_inner>article>table>tr:nth-child(6)>td").text[10:12]
        dict_infos_book['number_available'] = na
        if pd := sp.select_one(".product_page>p:nth-child(3)"):
            dict_infos_book['product_description'] = pd.text
        else:
            dict_infos_book['product_description'] = ""
        cat = sp.select_one("#default>div>div>ul>li:nth-child(3)>a").text
        dict_infos_book['category'] = cat
        rr = sp.select_one("#content_inner>article>table>tr:nth-child(7)>td").text
        dict_infos_book['review_rating'] = rr
        url_img = "http://books.toscrape.com/"+sp.find("img")['src'].strip("../../")
        dict_infos_book['image_url'] = url_img
    else:
        print("Informations non récupérées pour le libre dont l'url est : " + url)
    return dict_infos_book


def imprimer_infos_livre(livres, nom_fichier):
    """ print informations of a list of books in a .csv file """
    if not os.path.exists(DIR_FILES):
        os.mkdir(DIR_FILES)
    with open(DIR_FILES+'/'+nom_fichier+'.csv', mode='w', newline='', encoding="utf-8") as csv_file:
        fieldnames = ['product_page_url', 'universal_ product_code', 'title', 'price_including_tax',
                      'price_excluding_tax', 'number_available', 'product_description', 'category',
                      'review_rating', 'image_url']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(livres)


def telecharger_image(url, nom_image):
    """download a picture from a name and an url"""
    if not os.path.exists(DIR_IMAGES):
        os.makedirs(DIR_IMAGES)
    response = requests.get(url)
    if response.ok:
        with open(DIR_IMAGES + "/" + nom_image + ".jpeg", "wb") as file:
            file.write(response.content)
