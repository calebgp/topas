def main():
    teams = list(map(str, input().split()))
    goals = [0] * len(teams)
    for i in range(2):
        arr = list(map(int, input().split()))
        if i > 0:
            arr.reverse()
        goals[0] += arr[0]
        goals[1] += arr[1]
    print("-".join([str(x) for x in goals]))
    if goals[0] == goals[1]:
        print("penaltis")
        return
    winner = teams[goals.index(max(goals))]
    print(winner)
if __name__ == '__main__':
    main()