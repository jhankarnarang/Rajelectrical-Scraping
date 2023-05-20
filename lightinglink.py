import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}


lt_source = requests.get('https://rajelectricals.co.in/jointing-kits/',headers=headers)
lt_soup = BeautifulSoup(lt_source.content, 'lxml')
lt_main = lt_soup.find('div',class_='elementor-container elementor-column-gap-no')



# for lt_src in lt_main.find_all('div',class_='elementor-column-wrap elementor-element-populated'):
#     try:
#         lt_link = lt_src.p.a['href']
#         print(lt_link)
        
#     except:
#         print('')

for lt_src in lt_soup.find_all('div',class_='elementor-column-wrap elementor-element-populated'):
    try:
        lt_link = lt_src.p.a['href']
        print(lt_link)
        
    except:
        print('')

    
    # cr_source = requests.get(lt_link,headers=headers)
    # cr_soup = BeautifulSoup(cr_source.content, 'lxml')
    # for cr_main in cr_soup.find_all('div',class_='elementor-container elementor-column-gap-wide'):



    #     for src in cr_main.find_all('div',class_='elementor-column-wrap elementor-element-populated'):
    #         cr_img = src.div.figure.img['src']
    #         cr_name = src.div.h3.text
    #         print(f'Prod_Name - {cr_name} \nProd_img - {cr_img}')
            


    # for cr_main in cr_soup.find_all('div',class_='elementor-container elementor-column-gap-narrow'):



    #     for src in cr_main.find_all('div',class_='elementor-column-wrap elementor-element-populated'):
    #         cr_img = src.div.figure.img['src']
    #         cr_name = src.div.h3.text
    #         print(f'Prod_Name - {cr_name} \nProd_img - {cr_img}')
            
