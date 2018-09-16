from deribit_login import client
from time import sleep

yks = 1
buy_price = float(raw_input("buy price: "))
sell_amount = float(raw_input("amount of contracts: "))
trail_amount = float(raw_input("trail: "))
og_pp = buy_price

while yks == 1:
	sleep(1)
	price = client.getsummary('BTC-PERPETUAL')['midPrice']
	stoploss = buy_price - trail_amount
	if price > buy_price:
		buy_price = price
		profit = (stoploss - og_pp) * ((sell_amount * 10) / stoploss) 
		print("price: ", price)
		print("stoploss price: ",stoploss)
		print("trade size: ", sell_amount)
		print("p/l: ", profit)
		print("-----------------------------------")
	elif price < buy_price and price < stoploss:
		sell_price = client.getorderbook('BTC-PERPETUAL')['bids'][2]['price']
		client.sell('BTC-PERPETUAL', sell_amount,sell_price)
		yks = 2
		print("MYYTY")
		print("original buy price: ", og_pp)
		print("sell price: ", sell_price)
		
		
	
