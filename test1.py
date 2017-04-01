n = int(input("Number? "))

if n<0:
    if(n<-10):
        print("Number is less than -10")
    else:
        print("Number is greater than -10")
    print("Its a negative number")
elif n>0:
    print("Its a positive number")
else:
    print("ita zero")
