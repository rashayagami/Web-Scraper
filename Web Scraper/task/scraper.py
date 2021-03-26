import requests
from bs4 import BeautifulSoup
import json

url = input()
if url.__contains__("title"):
    link = requests.get(url)
    if 200 <= link.status_code < 400:
        s = BeautifulSoup(link.content, "html.parser")
        li = s.find("script", {"type": "application/ld+json"})

        # functions

        descriptionObj = s.find("div", {"class": "summary_text"})
        dic = json.loads(li.string)

        # function calls
        description = " ".join(descriptionObj.string.split())
        title = dic["name"]
        info = {"title": title, "description": description}
        print(info)
    else:
        print("Invalid movie page!")
else:
    print("Invalid movie page!")
