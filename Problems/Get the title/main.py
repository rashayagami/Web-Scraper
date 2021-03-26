import requests

from bs4 import BeautifulSoup
link = requests.get(input())
s = BeautifulSoup(link.content, 'html.parser')
li = s.find("h1")
print(li.text)
