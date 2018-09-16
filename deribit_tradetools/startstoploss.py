from deribit_login import client
from time import sleep

startstoploss = float(raw_input("start stoploss at: "))
stoploss = float(raw_input("stoploss sell price: "))
sell_amount = float(raw_input("amount of contracts: "))

yks = 1

while yks == 1:
	sleep(1)
	price = client.getsummary('BTC-PERPETUAL')['midPrice']
	print("price: ", price)
	print("starting stop loss at: ", startstoploss)
	if price >= startstoploss:
		while yks == 1:
			sleep(1)
			price = client.getsummary('BTC-PERPETUAL')['midPrice']
			print("current price", price)
			print("stop loss price", stoploss)
			if price <= stoploss:
				market_sell = stoploss - 50
				client.sell('BTC-PERPETUAL', sell_amount, market_sell)
				print("amount sold: ", sell_amount)
				break
		break	
