def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def P(n,r):
    return fact(n) / fact(n-r)
    
def P2(n,r):
    dolly = 1
    for i in range(n-r+1, n+1):
        dolly = dolly * i
    return dolly
    
def C(n,r):
    return P(n,r) / fact(r)
    
paul = int(input("What is n? "))
kylie = int(input("What is r? "))
pnr = P(paul,kylie)
cnr = C(paul,kylie)
pnr2 = P2(paul,kylie)

print("P(",paul,",",kylie,") =",pnr)
print("P2(",paul,",",kylie,") =",pnr2)
print("C(",paul,",",kylie,") =",cnr)







