from bs4 import BeautifulSoup
import requests
import os

playlist_link = (
    "https://www.youtube.com/playlist?list=PLQVvvaa0QuDcOdF96TBtRtuQksErCEBYZ"
)

source = requests.get(playlist_link).text

soup = BeautifulSoup(source, "lxml")
extension = set()
links = list()
for tag in soup.find_all("a"):
    if "href" in tag.attrs:
        if "watch?v=" in tag["href"]:
            if tag["href"] not in extension:
                extension.add(tag["href"])
                links.append("https://youtube.com" + tag["href"])

del links[0]
os.system("cls")
no_links = len(links)

print(f"Number of videos in playlist: {no_links}\n")
# print(f'Links for the videos:\n {links}\n')
for i in range(no_links):
   print(links[i])

##Writes the links to txt file
# with open('links.txt', 'w') as wf:
#     for link in links:
#         wf.write(f'{link}\n')

# #Link Opener
# from selenium import webdriver

# browser = webdriver.Firefox(
#     executable_path=r"C:\Users\Anoubhav\Desktop\python files\drivers\geckodriver.exe"
# )
# i = 0
# for link in links[-3:]:
#    if i==0:
#       browser.get(link)
#       i+=1
#    else:
#       browser.execute_script(f"window.open('{link}')")
