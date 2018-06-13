c=int(raw_input())
d=int(raw_input())
for num in range(c+1,d):
	if(num>1):
		for i in range(2,num):
			if(num%i==0):
				break
			else:
				print(num)
