from bs4 import BeautifulSoup
import requests

with open("index.html")as fp:
    soup=BeautifulSoup(fp,"html.parser")
    soup.find('h1')# this finds thed first <h1> tag
    soup.find_all('p')# finds all <p> tags
    tag=soupfind('a')


    #Accessing the attributes of a tag
    url=tag['href']# print the value of the href attribute

# EXTRACTING TEXT(we use the .text) 
print(heading.text)

