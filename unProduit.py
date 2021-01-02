import requests
import csv
from bs4 import BeautifulSoup


# scrap les informations  d'un livre à partir d'un lien 
def infosBook(url): 
    urlTravail = url
    dictInfosBook = {}
    
    response = requests.get(urlTravail)
    if response.ok:
        soup = BeautifulSoup(response.text , "html.parser") 
        
        dictInfosBook['product_page_url'] = urlTravail
        dictInfosBook['universal_ product_code'] = soup.select_one("#content_inner > article > table > tr:nth-child(1) > td").text
        dictInfosBook['title'] = soup.find('title').text
        dictInfosBook['price_including_tax'] = soup.select_one("table > tr:nth-child(4) > td:nth-child(2)").text
        dictInfosBook['price_excluding_tax'] = soup.select_one("#content_inner > article > table >  tr:nth-child(3) > td").text
        dictInfosBook['number_available'] = soup.select_one("#content_inner > article > table > tr:nth-child(6) > td").text
        dictInfosBook['product_description'] = soup.select_one(".product_page > p:nth-child(3)").text        
        dictInfosBook['category'] = soup.select_one("#default > div > div > ul > li:nth-child(3) > a").text
        dictInfosBook['review_rating'] = soup.select_one("#content_inner > article > table > tr:nth-child(7) > td").text
        dictInfosBook['image_url'] = soup.find('img')['src']

    return dictInfosBook

print(infosBook("http://books.toscrape.com/catalogue/set-me-free_988/index.html"))

def imprimeInfos (unlivre):
    with open('unLivre.csv', mode='w', encoding='utf-8') as csv_file:
       fieldnames = ['product_page_url', 'universal_ product_code', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
       writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

       writer.writeheader()
       writer.writerow(unlivre)


imprimeInfos(infosBook("http://books.toscrape.com/catalogue/set-me-free_988/index.html"))
