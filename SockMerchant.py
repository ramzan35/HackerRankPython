n = input();
c = [n];
count = 0;

for c_i in n:
    c[c_i] = input();

selected = {};

for j in selected.size:
    for i in selected.size:
        if (selected.get(j) == selected.get(i)):
            selected.remove(j);
            selected.remove(i - 1);
            count = count + 1;
            j = 0;
            i = 0;

print(count);
print(selected.toString());
