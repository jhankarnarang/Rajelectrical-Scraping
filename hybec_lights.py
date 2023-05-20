import requests
from bs4 import BeautifulSoup
import csv

csv_file = open('dowells.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product Name','Image Links'])

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}


cr_source = requests.get('https://rajelectricals.co.in/lighting/golden-apple/',headers=headers)
cr_soup = BeautifulSoup(cr_source.content, 'lxml')
for cr_main in cr_soup.find_all('div',class_='elementor-container elementor-column-gap-wide'):


    
    for src in cr_main.find_all('div',class_='elementor-column-wrap elementor-element-populated'):
        cr_img = src.div.figure.img['src']
        cr_name = src.div.h3.text
        print(f'Prod_Name - {cr_name} \nProd_img - {cr_img}')
        csv_writer.writerow([cr_name,cr_img])


for cr_main in cr_soup.find_all('div',class_='elementor-container elementor-column-gap-narrow'):



    for src in cr_main.find_all('div',class_='elementor-column-wrap elementor-element-populated'):
        cr_img = src.div.figure.img['src']
        cr_name = src.div.h3.text
        print(f'Prod_Name - {cr_name} \nProd_img - {cr_img}')
        csv_writer.writerow([cr_name,cr_img])
