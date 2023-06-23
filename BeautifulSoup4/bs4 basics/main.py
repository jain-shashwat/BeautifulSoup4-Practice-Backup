from bs4 import BeautifulSoup
import lxml

with open("index.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup)
# print(soup.prettify())

# print(soup.a)

all_h1 = soup.find_all(name="h3")
for tag in all_h1:
    # print(tag.getText())
    pass

all_anchor_tags = soup.find_all("a")
# print(all_anchor_tags)
for tag in all_anchor_tags:
    # print(tag.get("href"))
    pass

heading = soup.find(name="h1", id="name")
# print(heading)
# print(heading.text)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get("class"))

headings = soup.select(".heading")
print(headings)
name = soup.select_one("#name")
# print(name)





