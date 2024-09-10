print ("Enter Investment Amount:", end=' ')
Initial_balance = int(input())
print ("intrest percent", end=' ')
I = int(input())

N = 7

balance: float = ((Initial_balance*(1+I)**N)-Initial_balance)

print ("Yvonne's Compound interest after 7 years:", balance)