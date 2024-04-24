tMedia = int(input())
c = 0
nTemperatures = int(input())
temperatures = []
for i in range(nTemperatures):
    temperatures.append(int(input()))
for i in temperatures:
    if i > tMedia:
        c += 1
    else:
        c = 0
if c < 6:
    print("FLAT")
else:
    print("WAVE")
