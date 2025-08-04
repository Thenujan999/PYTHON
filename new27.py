t=int(input("no of units used"))
if t>0:
	if t<=1000:
		due=1*500
		print(due)
	elif t<=3000:	
		due=500+(t-1000)*3
		print(due)
	elif t<=10000:	
		due=500+2000*3+(t-3000)*5
		print(due)
	elif t>10000:	
		due=500+2000*3+7000*5+(t-10000)*10
		print(due)
else:
	print("invalid number")