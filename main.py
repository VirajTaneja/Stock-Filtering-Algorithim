from stocksymbol import StockSymbol
import yfinance as yf
from tqdm import tqdm
import bs4 as bs
import requests
from multiprocessing import *

api_key = " put your api key here "
ss = StockSymbol(api_key)

symbol_list_dow = ss.get_symbol_list(index="DJI")
symbol_list_nas = ss.get_symbol_list(index="IXIC")

# Can't find S&P falling back to slow workaround
resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = bs.BeautifulSoup(resp.text, 'lxml')
table = soup.find('table', {'class': 'wikitable sortable'})

tickers = []

for row in table.findAll('tr')[1:]:
    ticker = row.findAll('td')[0].text
    tickers.append(ticker.strip())

valids = []
for entry in symbol_list_dow:
	valids.append(entry["symbol"])
for entry in symbol_list_nas:
	valids.append(entry["symbol"])

valids = valids + tickers

def main(stock):
	try:
		main = yf.Ticker(stock.upper())
		hist = main.history(period="1d")
		if hist.iat[0,0] >= 3 and main.info["forwardPE"] >= 25 and main.info["trailingEps"] <= 0:
			gain = (hist.iat[0,3] - hist.iat[0,0]) / hist.iat[0,0]
			return gain, stock.upper()
		else:
			return False
	except:
		return False

if __name__ == '__main__':
	possibilities = {}
	maxes = []
	pool = Pool(16)
	with pool:
		for res in tqdm(pool.imap_unordered(main, valids), total=len(valids)):
			if res:
				gain, upp = res
				possibilities[gain] = upp
				maxes.append(gain)

	if len(maxes) == 0:
		print("better luck tommorow")
	elif len(maxes) <= 5:
		print("Couldn't find 5, here's all that were found")
		print(possibilities)
	else:
		max5 = []
		for _ in range(5):
			current_max = max(maxes)
			max5.append(possibilities[current_max])
			maxes[maxes.index(current_max)] = float("-inf")
		print(max5)
