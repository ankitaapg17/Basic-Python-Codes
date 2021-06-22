def findlcm(a,b):
    if(a>b):
        maximum=a
    else:
        maximum=b

    while(True):
        if(maximum % a == 0 and maximum % b == 0):
            lcm = maximum
            break
        maximum=maximum+1 #if lcm not found then generate next multiple of max bw both numbers
    return lcm

#Taking inputs from the user
num1 = int(input())
num2 = int(input())
lcm=findlcm(num1,num2)
print(lcm)