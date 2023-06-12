from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('step-lights.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Image Links','Product Description'])

l=[]
m=[]
source = requests.get('https://finolex.com/optical-fibre-cables/')
soup = BeautifulSoup(source.content, 'lxml')

for main1 in soup.find_all('div',class_='col-sm-4'):
    try :
        img1 = main1.img['src']
        if 'pdf.png' not in img1:
            print(img1)
            
            l.append(img1)
    
    except:
        print('')

    
        
    info1 = main1.text
    
    desc1 = info1.replace('Download Brochure(PDF 2.2MB)','')
    prod_desc1 = (''.join(desc1.splitlines()))
    print(desc1)
    
    m.append(prod_desc1)
 
while(" " in l) :
    l.remove(" ")

while("" in l) :
    l.remove("")
w = str(l)

print(len(w))


while(" " in m) :
    m.remove(" ")

while("" in m) :
    m.remove("")
    x= str(m)
csv_writer.writerow([w,x])
        
print(len(x))

