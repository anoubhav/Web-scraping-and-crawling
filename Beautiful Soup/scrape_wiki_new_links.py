from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random

unique_pages = set()


def getLinks(articleURL):

   global unique_pages
   html = urlopen("http://en.wikipedia.org" + articleURL)
   soup = BeautifulSoup(html, "lxml")

   for links in soup.find("div", id="bodyContent").find_all("a"):
      if "href" in links.attrs:
         if "/wiki/" in links["href"] and ":" not in links["href"]:
            if links["href"] not in unique_pages:
               newpage = links["href"]
               print(newpage)
               unique_pages.add(newpage)
               getLinks(newpage)


getLinks("")
