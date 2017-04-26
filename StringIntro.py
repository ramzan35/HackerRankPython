
A = input();
B = input();

length = A.length() + B.length();

print(length);

if (A.compareTo(B) > 0):
    System.out.println("Yes");
else:
    System.out.println("No");

if (A.compareTo(B) < 0):
    print(
        A.substring(0, 1).toUpperCase() + A.substring(1) + " " + B.substring(0, 1).toUpperCase() + B.substring(1));
else:
    print(
        B.substring(0, 1).toUpperCase() + B.substring(1) + " " + A.substring(0, 1).toUpperCase() + A.substring(1));
