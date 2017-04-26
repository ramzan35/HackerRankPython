value = input()
ithuru = 0
cons = 0
maxCons = 0

while (true):
    ithuru = value % 2;
    value = value / 2;
    if (ithuru == 1):
        cons = cons + 1;
    if (maxCons < cons):
        maxCons = cons;
    else:
        cons = 0;

    if (value == 0):
        break;
    elif (value == 1):
        cons = cons+1;
        if (maxCons < cons):
            maxCons = cons;
        break;

    print(maxCons);
