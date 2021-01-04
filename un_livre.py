import requests
import csv
from bs4 import BeautifulSoup


# scrap les informations  d'un livre à partir d'une url
def infos_book(url):
    dict_infos_book = {}
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        dict_infos_book['product_page_url'] = url
        dict_infos_book['universal_ product_code'] = soup.select_one("#content_inner > article > table > tr:nth-child(1) > td").text
        dict_infos_book['title'] = soup.find('title').text.strip("\n  ").rstrip("\n")
        dict_infos_book['price_including_tax'] = soup.select_one("table > tr:nth-child(4) > td:nth-child(2)").text.strip("Â")
        dict_infos_book['price_excluding_tax'] = soup.select_one("#content_inner > article > table >  tr:nth-child(3) > td").text.strip("Â")
        dict_infos_book['number_available'] = soup.select_one("#content_inner > article > table > tr:nth-child(6) > td").text[10:12]
        dict_infos_book['product_description'] = soup.select_one(".product_page > p:nth-child(3)").text.replace("â\x80\x99", "'")
        dict_infos_book['category'] = soup.select_one("#default > div > div > ul > li:nth-child(3) > a").text
        dict_infos_book['review_rating'] = soup.select_one("#content_inner > article > table > tr:nth-child(7) > td").text
        dict_infos_book['image_url'] = soup.find('img')['src']

    return dict_infos_book


# imprimer les infos d'un livre contenu dans une liste au sein d'un fichier CSV
def imprime_infos(un_livre, nom_fichier):
    with open(nom_fichier+'.csv', mode='w', encoding='utf-8') as csv_file:
        fieldnames = ['product_page_url', 'universal_ product_code', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(un_livre)):
            writer.writerow(un_livre[i])


imprime_infos([infos_book("http://books.toscrape.com/catalogue/a-summer-in-europe_458/index.html")], 'unlivre')
