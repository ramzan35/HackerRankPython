n = input();
flag = true;
i = 2;
for i in n:
    if (n % i == 0):
        print("not prime");
        flag = false;
        break;
if (flag):
    print ("prime");
