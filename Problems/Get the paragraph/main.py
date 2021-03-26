import requests

from bs4 import BeautifulSoup
word = input()
res = requests.get(input())
s = BeautifulSoup(res.content, "html.parser")
paras = s.find_all("p")
for p in paras:
    if p.text.__contains__(word):
        print(" ".join(str(p.text).split()))
