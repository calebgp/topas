f = int(input())
n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
drawn_number = None
for number in numbers:
    if number <= f:
        if drawn_number is None or drawn_number > number:
            drawn_number = number
if drawn_number is None:
    print("No free lunch")
else:
    print(drawn_number)