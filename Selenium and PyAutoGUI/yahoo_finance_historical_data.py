# Importing libraries
from selenium import webdriver
import pandas as pd
import os, time
import datetime as dt

# Loads companylist dataset from nyse and nasdaq in a pandas dataframes and concatenate them
df_nasdaq = pd.read_csv('companylistnasdaq.csv')
df_nyse = pd.read_csv('companylistnyse.csv')
del df_nasdaq[df_nasdaq.columns[-1]]
del df_nyse[df_nyse.columns[-1]]
df = pd.concat([df_nasdaq, df_nyse])

# Creating a set of all tickers 
df['MarketCap'] = df['MarketCap'].apply(lambda x: float(x)/10**6)
ticker_list = set(df['Symbol'])

os.system('cls')

# Takes input from user
ticker = input('Enter ticker: ')
ticker = ticker.upper()

# Checks if ticker is valid
if ticker in ticker_list:
    print('\n',df[df['Symbol'] == ticker].to_string(index = False))
else:
    print('Invalid ticker')
    quit()

# Prompts the user for downloading historical data
user_input = input('\nDo you want to download historical data for {} (Y/n)? '.format(df[df['Symbol'] == ticker]['Name'].to_string(index = False)))

if user_input == 'n':
    print('Exiting program')
    quit()

elif user_input == 'Y':

    # User input
    print('\nEnter the duration in mm/dd/yyyy format')
    start_date = input('Start date:')
    end_date = input('End date (T for today):')
    frequency = input('Frequency (1d/1w/1mo):')

    try:
        # Convert start-date and end-date input(string) into epoch time
        ts = time.strptime(start_date, '%m/%d/%Y')
        start_stamp = str(time.mktime(ts))
        
        if end_date == 'T':
            today = dt.date.today()
            end_date = '{}/{}/{}'.format(today.month, today.day, today.year)
        ts = time.strptime(end_date, '%m/%d/%Y')
        end_stamp = str(time.mktime(ts))

    except Exception as e:
        print(e)
        quit()
    website_url = 'https://in.finance.yahoo.com/quote/'+ ticker + '/history?period1='+ start_stamp + '&period2=' + end_stamp + '&interval=' + frequency + '&filter=history&frequency=' + frequency
    
    # Opens Chrome browser and loads yahoo finance website
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')
    browser = webdriver.Chrome(executable_path=r"C:\Users\Anoubhav\Desktop\python files\drivers\chromedriver.exe", chrome_options=options)
    browser.set_page_load_timeout(20)
    browser.implicitly_wait(20)
    browser.maximize_window()
    try:
        browser.get(website_url)
    except Exception as e:
        print(e)
        quit()

    # Finding the 'download data' link on the webpage
    elem = browser.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a')
    elem.click()
        
    time.sleep(5)
    browser.quit()
else:
    print('Invalid input')
    quit()







