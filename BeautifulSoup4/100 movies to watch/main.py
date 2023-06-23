import json
import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movies_webpage = response.text
soup = BeautifulSoup(movies_webpage, "html.parser")
data = json.loads(soup.select_one(selector="#__NEXT_DATA__").contents[0])
data_dict = data["props"]["pageProps"]["apolloState"]
for a, b in data_dict.items():
    if a.startswith("ImageMeta"):
        print(b["titleText"])
# import requests
# from bs4 import BeautifulSoup
#
# URL = "https://www.empireonline.com/movies/features/best-movies-2/"
#
# response = requests.get(URL)
# website_html = response.text
#
# soup = BeautifulSoup(website_html, "html.parser")
# soup.prettify()
#
# all_movies_name = soup.select(class_="jsx-4245974604")
#
# print(all_movies_name)
#
# # movies_list = [movie.getText() for movie in all_movies_name]
# # print(movies_list)
#
#
