while True:
    i = input("what math are we doing:")
    n1 = int(input("number 1:"))
    n2 = int(input("number 2:"))
    if i=="+":
        a=(n1+n2)
    elif i=="-":
        a=(n1-n2)
    elif i=="*":
        a=(n1*n2)
    elif i=="/":
        a=(n1/n2)
    elif i=="**":
        a=(n1**n2)
    print(n1,i,n2,"=",a)

          