a=1
s=0

print('Enter numbers to add the sum')
print('Enter 0 to quit')

while a!=0:
    print('Current Sum:',s)
    a = int(input('Number ? '))
    s += a
print('Total sum = ',s)    
