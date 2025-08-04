'''y=int(input("enter your marks"))
if y>50:
	print("pass")
else:
	print("fail")'''
'''x=int(input("enter your marks"))
if x>75:
    print("A")
elif x>65:
    print("B")
elif x>55:
    print("C")
elif x>45:
    print("S")
else:
    print("fail") '''     
    
'''x=int(input("enter your marks"))
if x<=100 and x>=0:
    if x>75:
        print("A")
    else:
        if x>65:
            print("B")
        else:
            if x>55:
                print("C")
            else:
                if x>45:
                    print("S")    
                else:   
                    print("fail")
else:
    print("invalid number")'''
t=int(input("enter your call minutes"))
if t<=120 and t>0:
    if t<=30:
        due=t*2
        print(due)
    elif t<=60:
        due=30*2+(t-30)*1.5
        print(due)
    elif t<=120:
        due=30*2+(t-60)*1+(30*1.5)
        print(due)                  
else:
    print("invalid number")