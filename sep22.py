def fact(n):
	if n == 0:
		return 1 
	else:
		return n * fact(n-1)

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
        
ephraim = int(input("Give me a number: "))
cellestin = fact(ephraim)
print("Factorial of",ephraim,"is:",cellestin)
nora = fib(ephraim)
print("Fib(",ephraim,") =",nora)






