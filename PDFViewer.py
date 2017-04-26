h = [26];
for h_i in 26:
    h[h_i] = input();

word = input();
height = 0;
heighest = 0;
max_h = 0;
res = 0;

for i in word.length:
    res = (int)
word.charAt(i);
res = res % 48;
if (h[res - 1] < max_h):
    pass;
else:
    max_h = h[res - 1];

print(max_h * word.length());
