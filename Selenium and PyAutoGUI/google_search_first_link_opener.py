from selenium import webdriver

user_input = input('What should I google for you today ?\n')
browser = webdriver.Chrome(executable_path=r"C:\Users\Anoubhav\Desktop\python files\drivers\chromedriver.exe")
browser.set_page_load_timeout(20)
browser.get('https://www.google.com/')
browser.implicitly_wait(20)

# Locates the search bar, enters the text and submits the request
elem = browser.find_element_by_css_selector('#lst-ib')
elem.send_keys(user_input)
elem.submit()
# Locates the first website and visits it
elem = browser.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/div/h3/a')
elem.click()
# browser.quit()

