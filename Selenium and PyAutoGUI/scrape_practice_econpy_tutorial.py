from selenium import webdriver
import pandas as pd

max_page_num = 5
max_page_dig = 3

browser = webdriver.Chrome(executable_path=r"C:\Users\Anoubhav\Desktop\python files\drivers\chromedriver.exe")
browser.set_page_load_timeout(30)
browser.implicitly_wait(20)

buyers_lst = list()
prices_lst = list()

for i in range(1,max_page_num+1):
   page_num = (max_page_dig - len(str(i)))*'0'+str(i)
   url = 'http://econpy.pythonanywhere.com/ex/'+page_num+'.html'
   browser.get(url)

   buyers = browser.find_elements_by_xpath('//div[@title="buyer-name"]')
   prices = browser.find_elements_by_xpath('//span[@class="item-price"]')

   for i in range(len(buyers)):
      buyers_lst.append(buyers[i].text)
      prices_lst.append(prices[i].text)

df = pd.DataFrame({'Buyer': buyers_lst, 'Price':prices_lst})
print(df)
df.to_excel('scrape_econpy_tutorial.xlsx')
browser.quit()