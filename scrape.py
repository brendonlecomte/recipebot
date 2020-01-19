#! /Users/brendonlc/research/recipbot/bin/python
import requests
from bs4 import BeautifulSoup
headers = {'User-agent': 'Mozilla/5.0'}

# searchPath = 'https://www.bbcgoodfood.com/search/recipes?query=vegan&page={}'
searchPath = 'https://www.bbcgoodfood.com/search/recipes?query=&page={}'

with open("mains-recipes.txt", "w") as f:
    for x in range(0, 860):
        page = requests.get(searchPath.format(x), headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        links = soup.find_all("h3", "teaser-item__title", 'a href')
        for link in links:
            print(str(link.a["href"]))
            f.write(str(link.a["href"]))
            f.write("\n")

