from time import sleep
from deribit_login import client

buy_amount = float(raw_input("contract quantity: "))
time_interval = int(raw_input("time interval (minutes): "))
total_bought = 0
counter = 0
total_time = 0
yks = 1
while yks == 1:
	try:
		askprice = client.getorderbook('BTC-PERPETUAL')['asks'][1]['price']
		client.buy('BTC-PERPETUAL', buy_amount, askprice)
		total_bought += buy_amount
		counter += 1
		timer = time_interval * 60
		print("total_bought: ", total_bought,"times: ", counter, "\n buys in minutes: ", buy_amount , time_interval, "\n total time:", total_time  )
		sleep(timer)
		total_time += time_interval
	except:
		print("massit loppu lol, hyvin menee")
		sleep(5) 
