I1, D1, I2, D2 = map(int, input().split())

t1 = float(f"{I1}.{D1}")
t2 = float(f"{I2}.{D2}")

if t2 < 37:
    print("NORMAL")
else:
    out = "FEBRE"

    if t1 < t2:
        out += "MAIOR"
    elif t1 > t2:
        out += "BAIXOU"
    else:
        out += "MANTEVE"
    print(out)
