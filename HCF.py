def compute_hcf(x,y):
    #choose smaller number
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1, smaller+1):
        if((x%i==0)and(y%i==0)):
            hcf=i
    return hcf

num1=int(input())
num2=int(input())
print("The HCF is",compute_hcf(num1,num2))