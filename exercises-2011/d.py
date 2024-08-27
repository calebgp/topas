key = input()
tried = input()
right_placed = 0
wrong_placed = 0
res_tries = []
res_key = []
for i in range(len(key)):
    if key[i] == tried[i]:
        right_placed += 1
        continue
    res_key.append(key[i])
    res_tries.append(tried[i])
for c in res_tries:
    if c in res_key:
        wrong_placed += 1
        res_key.remove(c)
print(right_placed)
print(wrong_placed)