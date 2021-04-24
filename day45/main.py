from bs4 import BeautifulSoup
import lxml

with open("website.html") as web_page:
    result = web_page.read()

soup = BeautifulSoup(result, "lxml")
print(soup.title.string)
print(soup.a.string)