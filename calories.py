import requests
from bs4 import BeautifulSoup
headers = {'User-agent': 'Mozilla/5.0'}

# adding the saved recipe links to this base gives the page
basePath = 'https://www.bbcgoodfood.com{}'


with open("mains-recipes.txt", "r") as f:
    with open("nutrition.txt", "w") as out:
        i = 0
        for x in f.readlines():
            i += 1
            page = requests.get(basePath.format(x.strip()), headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')

            # inspect element on the page. Find what you need specifically
            links = soup.find_all("span", "nutrition__value")
            try:  # try parse out calories, protein, and fat
                calories = int(links[0].text)
                protein = float(links[6].text[:-1])
                fat = int(links[1].text[:-1])

                # crude filter on requirements
                if calories > 340 and calories < 560 and protein > 25 and fat < 20:
                    print(f"{i}: {basePath.format(x.strip())}")
                    out.write(f"{i}: {basePath.format(x.strip())}\n")
                    print(f"\t{calories}kcal, {protein}")
                    out.write(f"\t{calories}kcal, {protein}\n")
            except:
                print(f"{i}: {x.strip()} failed")
