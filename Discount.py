#Enter 5 item cost if sum of 5 item cost is >=5000 then give 10% discount and display total amount paid else 5% discount
sum=0
for x in range(0,6):
    amt = int(input("Enter sale amount: "))
    sum=sum+amt



if sum>=5000:
    dis=0.1*sum
    print("The final amount is:",sum-dis)

else:
    dis=0.05*sum
    print("The final amount is:",sum-dis)

