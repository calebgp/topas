n = int(input())
c = 0
price = int(input())
for i in range(n):
    arr = list(map(int, input().split()))
    for p in arr:
        if p > price:
            c += 1
            break
    price = arr[-1]
print(c)
