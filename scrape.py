import requests
from bs4 import BeautifulSoup

# Some websites dislike not having a header that looks like a web browser
headers = {'User-agent': 'Mozilla/5.0'}

# carefully constructed search path allows us to look for the results we want
# this could be changed for any website. Below is just for bbc good food
searchPath = 'https://www.bbcgoodfood.com/search/recipes?query=&page={}'

with open("mains-recipes.txt", "w") as f:
    for x in range(0, 860):  # 860 is the number of pages this result produces (at the time of commit)

        # Generic request and parse
        page = requests.get(searchPath.format(x), headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        # looked at the website and its returned data.
        # This search gets me the objects I want. Recipe results
        links = soup.find_all("h3", "teaser-item__title", 'a href')

        for link in links:
            print(str(link.a["href"]))  # print the returned recipe path
            f.write(str(link.a["href"]))  #dump to file
            f.write("\n")

