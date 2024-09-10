print ('Enter Investment Amount:', end=' ')
Initial_balance = int(input())
print ('Enter Intrest Percent:', end=' ')
I = float(input())
print('Enter Years To Grow:', end=' ')
N = int(input())

balance: float = ((Initial_balance*(1+I)**N)-Initial_balance)

print ('Compound interest after',N, 'years:', balance)