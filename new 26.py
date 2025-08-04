t=int(input("no of units used"))
if t>0:
	if t<=90:
		due=t*7
		print(due)
	elif t<=150:	
		due=90*7+(t-90)*10
		print(due)
	elif t<=300:	
		due=90*7+60*10+(t-150)*15
		print(due)
	elif t>300:	
		due=90*7+60*10+150*15+(t-300)*15+(90*7+60*10+150*15+(t-300)*15)*3/100
		print(due)
else:
	print("invalid number")