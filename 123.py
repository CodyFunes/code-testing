

BR=int(input("What is the birth rate in terms of seconds: "))
DR=int(input("What is the death rate in terms of seconds: "))
IR=int(input("What is the immigration rate in terms of seconds: "))
CRP=int(input("What is the current population?: "))
Fut=int(input("How many years into the future for the population would you like to see: "))


SecInYear=365*24*60*60
TPITF= round(CRP+((SecInYear/BR)-(SecInYear/DR)+(SecInYear/IR))*Fut)

print("The birth rate is ", BR)
print("The death rate is ", DR)
print("The immigration rate is ", IR)
print("The current population is ", CRP)
print("You want to see the population in ", Fut, " years")

print(f'{TPITF:,}')

if CRP>TPITF:
    print("Your population has decreased")
else:
    print("Your population has increased")

