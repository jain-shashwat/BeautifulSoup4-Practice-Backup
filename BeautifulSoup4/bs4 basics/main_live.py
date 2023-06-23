from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

web_page = response.text


soup = BeautifulSoup(web_page, "html.parser")
article = soup.find_all(name="span", class_="titleline")

article_text = []
article_link = []
for tag in article:
    text = tag.getText()
    article_text.append(text)
    article_section = tag.select("a")
    link = article_section[0].get("href")
    article_link.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name = "span", class_="score")]
# print(article_text)
# print(article_link)
# print(article_upvote)

index = article_upvote.index(max(article_upvote))
print(index)
print(article_text[index])
print(article_link[index])






