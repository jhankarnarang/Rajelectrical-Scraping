import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}


source = requests.get('https://rajelectricals.co.in/',headers=headers)
soup = BeautifulSoup(source.content, 'lxml')
main = soup.find('div',class_='elementor-container elementor-column-gap-no')



for src in main.find_all('div',class_='elementor-column-wrap elementor-element-populated'):
    try:
        link = src.a['href']
        print(link)
        
    except:
        print('')

    

    lt_source = requests.get(link,headers=headers)
    lt_soup = BeautifulSoup(lt_source.content, 'lxml')
    lt_main = lt_soup.find('div',class_='elementor-container elementor-column-gap-no')



    for lt_src in lt_main.find_all('div',class_='elementor-column-wrap elementor-element-populated'):
        try:
            lt_link = lt_src.p.a['href']
            print(lt_link)
            
        except:
            print('')
    