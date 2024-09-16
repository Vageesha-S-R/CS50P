p=50
t=0
c=[25,10,5]

while p>0:
    print("Amount Due:",p)
    pay=int(input("Insert Coin: "))
    if pay in c:
        p=p-pay
        t=t+pay

if t>=p:
    print("Change Owed:",t-50)
