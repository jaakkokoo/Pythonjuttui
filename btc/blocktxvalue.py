from subprocess import check_output
import json

total_output = 0 
number_output = 0 

block = int(raw_input("Give block height: "))
blockhash = check_output(["bitcoin-cli", "getblockhash",str(block)]) 
blockdata = check_output(["bitcoin-cli","getblock", blockhash]) 
blockdatajson = json.loads(blockdata)  
for transaktio in blockdatajson['tx']: 
	rawtx = check_output(["bitcoin-cli", "getrawtransaction",transaktio]) 
	rawtx = rawtx[:-1] 
	decodedtx = check_output(["bitcoin-cli", "decoderawtransaction", rawtx]) 
	decodedjson = json.loads(decodedtx) 
	number_output = number_output + 1  
	for output in decodedjson['vout']:
		total_output = total_output + output['value'] 
		

print("Blockhash: ", blockhash ,  "Number of outputs:  ", number_output , "Output total sum:  ", total_output)
