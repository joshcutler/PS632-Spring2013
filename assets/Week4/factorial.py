def factorial(x): 
	return 1 if x==1 else x*factorial(x-1)

print factorial(1)
print factorial(2)
print factorial(3)
print factorial(6)