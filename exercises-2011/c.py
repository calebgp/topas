n, m = map(int, input().split())
mat = [[int(j) for j in list(input())] for i in range(n)]
output = []
for i in range(m):
    arr = []
    for j in range(n):
        arr.append(mat[j][i])
    summ = sum(arr)
    if summ == n or summ <= n / 2:
        output.append(0)
        continue
    output.append(1)
print("".join(map(str, output)))
