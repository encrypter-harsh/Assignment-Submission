

g=input("Enter F/f for female or M/m for male: \n")

c=input("Enter S/s for Senior citizen or N/n for Non senior citizen: \n")

a=int(input("Enter your principle amount \n"))

t=int(input("Enter your time of Fixed Deposit"))
i=0

if g=="f" or g=="F":
	if c=="S"or c="s":
		i= (a*t*8)/100
	elif:
		c=="N"or c="n":
		i=(a*t*6)/100
	else:
		print("Enter correct citizen choice")
elif  g=="M" or g=="m":
	if c=="S"or c="s":
		i= (a*t*7)/100
	elif:
		c=="N"or c="n":
		i=(a*t*5)/100
	else:
		print("Enter correct citizen choice")
	
else:
	print("Enter correct gender choice")

print("The interest will be",i)

	
