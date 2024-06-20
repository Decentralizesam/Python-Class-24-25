from bs4 import BeautifulSoup
import requests


url="https://dihfahsih.com"
response=requests.get(url)
if response.status_code==200:
    # parsing the html content 
    soup=BeautifulSoup(response.text, 'html.parser')
    # Extract and print the title of the page 
    paragraph=soup.find('p',class_='text-muted').text
    Name=soup.find('h1',class_='text-white font-weight-bold').text
    head2=soup.find('h2',class_='text-light').text
    print(f'Paragraph:{paragraph},Name:{Name},Header:{head2}')
    #Extract and printging the all the links on the page
    #links=soup.find_all('a')
    #for Link in links:
        #href=Link.get('href')
        #text=Link.text
        #print(f"Link text:{text},Url:{href}")

else:
        print(f"Failed to retrive the web page. Error :{response.status_code}")