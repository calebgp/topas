
def calc_weight(arr):
    sum_weight = 0
    for m in arr:
        if m > 2:
            weight = 1
        else:
            weight = 5
        sum_weight += weight
    return sum_weight


total_weight, d = map(int, input().split())
money_array = [int(input()) for _ in range(d)]
actual_weight = calc_weight(money_array)
rest_weight = total_weight - actual_weight
print(rest_weight)
notes = rest_weight // 5
print(notes)

