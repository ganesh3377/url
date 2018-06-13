a=int(raw_input())
b=int(raw_input())
def arms(a):
	b=a%10
	e=a/10
	c=e%10
	d=e/10
	f=b**3+c**3+d**3
	if(f==a):
		print(num)
for num in range(a,b+1):
	y=arms(num)
