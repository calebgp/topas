r = int(input())
m = int(input())
c = 0

while True:
    if m / r == 2:
        break
    else:
        c += 1
        m += 1
        r += 1
print(c)