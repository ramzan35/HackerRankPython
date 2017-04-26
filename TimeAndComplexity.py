rD = input();
arr = [rD];

for i in arr.length:
    arr[i] = sc.nextInt();

flag = true;
for i in arr.length:
    flag = true;
if (arr[i] <= 1):
    flag = false;

elif (arr[i] <= 4):
    for j in arr.length:
        if (arr[i] % 2 == 0 | arr[i] % 3 == 0):
            flag = false;
