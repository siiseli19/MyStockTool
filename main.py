
#Only for individual use
#Analysed results should not be considered as financial advide.
#Always do your own research.


import requests
from bs4 import BeautifulSoup


#Extra feature when everything else is done
#In case user has no idea what stocks to analyze
#multiple parameters used as filters (sector, market cap etc).
#returns a list of 50 XX-market value stocks
def potential_stocks_finder():
    pass



#Function to extract stock data from yahoofinance.com
#Takes a stocks ticker as a parameter
#How to take account changing years on page??
def extract_stock_info(ticker):

    ticker = 'LOW'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    url = 'https://finance.yahoo.com/quote/'+ticker
    r = requests.get(url)
    print(r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')




#Transform scrabed data
#Takes data as parameter and
def transform_data():
    pass


#Driver function with cmd-line based gui with while-loop for multiple analysis
def commandline_gui():

    choice = None
    while True:


        try:
            choice = str(input().upper())

        except:
            print('Something went wrong :(')







extract_stock_info('pg')