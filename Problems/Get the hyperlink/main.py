import requests

from bs4 import BeautifulSoup
r = requests.get("http://www.gutenberg.org/files/3825/3825-h/3825-h.htm")
soup = BeautifulSoup(r.content, 'html.parser')
li = soup.find_all("a")
print(type(li))
print(li[0].get("href"))
print(li)
