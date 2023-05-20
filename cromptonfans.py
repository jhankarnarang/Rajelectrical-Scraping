from bs4 import BeautifulSoup
import requests
import csv

# csv_file = open('step-lights.csv','w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Product Name','Image Links','Product Description','Available Wattage'])


cr_source = requests.get('https://rajelectricals.co.in/')
cr_soup = BeautifulSoup(cr_source.content, 'lxml')
cr_main = cr_soup.find_all('div',class_='elementor-container elementor-column-gap-wide')
print(cr_soup.prettify)


# for src in cr_main.find('figure',class_='elementor-image-box-img'):
#     print(src)
    
    # csv_writer.writerow([name,img,info])
