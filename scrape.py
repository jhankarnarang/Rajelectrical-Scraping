from bs4 import BeautifulSoup
import requests
import csv


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

def scrape(sections, file_names):
    for i in range(len(sections)):
        with open(file_names[i], 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['name', 'img'])

            print(f'> {sections[i]}')
            section_source = requests.get(sections[i])
            section_page = BeautifulSoup(section_source.content, 'lxml')
            cr_source = requests.get(sections[i],headers=headers)
            cr_soup = BeautifulSoup(cr_source.content, 'lxml')
            for cr_main in cr_soup.find_all('div',class_='elementor-container elementor-column-gap-wide'):
                try:
                    for src in cr_main.find_all('div',class_='elementor-column-wrap elementor-element-populated'):
                        cr_img = src.div.figure.img['src']
                        cr_name = src.div.h3.text
                        print(f'Prod_Name - {cr_name} \nProd_img - {cr_img}')
                        csv_writer.writerow([cr_name,cr_img])
                except:
                    print('')


            for cr_main in cr_soup.find_all('div',class_='elementor-container elementor-column-gap-narrow'):


                try:

                    for src in cr_main.find_all('div',class_='elementor-column-wrap elementor-element-populated'):
                        cr_img = src.div.figure.img['src']
                        cr_name = src.div.h3.text
                        print(f'Prod_Name - {cr_name} \nProd_img - {cr_img}')
                        csv_writer.writerow([cr_name,cr_img])
                except:
                    print('')


            

            
            


if __name__ == '__main__':

    '''
    usage:
    -> install requirements
    -> verify:
        - all site sections are listed in `sections`
        - all sites have a corresponding csv file `file_names`
        - all paths to the csv file are correct
    -> run
    '''

    sections = [
        'https://rajelectricals.co.in/hybec-lighting/',
        'https://rajelectricals.co.in/lighting/endo-lights/',
        'https://rajelectricals.co.in/lighting/digiopto-lights-2/',
        'https://rajelectricals.co.in/lighting/golden-apple/',
        'https://rajelectricals.co.in/lighting/legero-lights-2/',
        'https://rajelectricals.co.in/lighting/havells-lighting/',
        'https://rajelectricals.co.in/lighting/pasolite/',
        'https://rajelectricals.co.in/lighting/phillips/',
        'https://rajelectricals.co.in/lighting/osram-lights-2/',
        'https://rajelectricals.co.in/lighting/archisa-lights-2/',
        'https://rajelectricals.co.in/crompton-fans/',
        'https://rajelectricals.co.in/almonard-fans/',
        'https://rajelectricals.co.in/aera-fans/',
        'https://rajelectricals.co.in/havells-fan/',
        'https://rajelectricals.co.in/orient-fans/',
        'https://rajelectricals.co.in/usha-fans/',
        'https://rajelectricals.co.in/gorilla-fans/',
        'https://rajelectricals.co.in/wadbros-fans/', 
        'https://rajelectricals.co.in/anchor-switches/',
        'https://rajelectricals.co.in/norisys-switches/',
        'https://rajelectricals.co.in/lt-switches/',
        'https://rajelectricals.co.in/legrand-switches/',
        'https://rajelectricals.co.in/havells-switches/',
        'https://rajelectricals.co.in/whitelion-switches/',
        'https://rajelectricals.co.in/hager-switches/',
        'https://rajelectricals.co.in/schneider-switches/',
        'https://rajelectricals.co.in/hager/',
        'https://rajelectricals.co.in/lt-mcbs-switchgears/',
        'https://rajelectricals.co.in/hpl/',
        'https://rajelectricals.co.in/legrand-switchgears/',
        'https://rajelectricals.co.in/polycab-cables-wires/',
        'https://rajelectricals.co.in/rr-kabel-wires-cables/',
        'https://rajelectricals.co.in/kei/',
        'https://rajelectricals.co.in/polytex-wire-cables/',
        'https://rajelectricals.co.in/finolex-wires-cables/',
        'https://rajelectricals.co.in/water-heater-geyser/',
        'https://rajelectricals.co.in/diamond/',
        'https://rajelectricals.co.in/precision/',
        'https://rajelectricals.co.in/jyoti/',
        'https://rajelectricals.co.in/3m/',
        'https://rajelectricals.co.in/raychem/',
        'https://rajelectricals.co.in/dowells/',
        'https://rajelectricals.co.in/cable-trays-2/'
           ]

    file_names = [
        './data/lighting/hybec-lighting.csv',
        './data/lighting/endo-lights.csv',
        './data/lighting/digi-opto.csv',
        './data/lighting/golden-apple.csv',
        './data/lighting/legero-lights.csv',
        './data/lighting/havells-lighting.csv',
        './data/lighting/pasolite.csv',
        './data/lighting/philips.csv',
        './data/lighting/osram-lights.csv',
        './data/lighting/archisa-lights.csv',
        './data/fans/crompton-fans.csv',
        './data/fans/almonard-fans.csv',
        './data/fans/aera-fans.csv',
        './data/fans/havells-fans.csv',
        './data/fans/orient-fans.csv',
        './data/fans/usha-fans.csv',
        './data/fans/gorilla-fans.csv',
        './data/fans/wardbros-fans.csv',
        './data/switches/anchor-switches.csv',
        './data/switches/norisys-switches.csv',
        './data/switches/lt-switches.csv',
        './data/switches/legrand-switches.csv',
        './data/switches/havells-switches.csv',
        './data/switches/whitelion-switches.csv',
        './data/switches/hager-switches.csv',
        './data/switches/schneider-switches.csv',
        './data/mcb/hager-mcb.csv',
        './data/mcb/lt-mcb-switchgear.csv',
        './data/mcb/hpl-switchgear.csv',
        './data/mcb/legrand-switchgear.csv',
        './data/wirescables/polycab.csv',
        './data/wirescables/rr-kabel.csv',
        './data/wirescables/kei.csv',
        './data/wirescables/polytex.csv',
        './data/wirescables/finolex.csv',
        './data/water-heater&geysers.csv',
        './data/conduits/diamond.csv',
        './data/conduits/precision.csv',
        './data/conduits/jyoti.csv',
        './data/jointingkits/3M.csv',
        './data/jointingkits/raychem.csv',
        './data/glands-lugs/dowells.csv',
        './data/cabletrays.csv'
    ]

    scrape(sections, file_names)