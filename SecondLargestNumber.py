if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

arr.sort()
arr.reverse()


nmb = arr[0]

for num in arr:
    if num != nmb:
        print(num)
        break
