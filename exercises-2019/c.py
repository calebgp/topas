def check_alibi(kill_start, kill_end, alibi_start, alibi_end):
    return alibi_start >= kill_start and alibi_end <= kill_end


n = int(input())
for _ in range(n):
    crime_start, crime_end = map(int, input().split())
    suspect_start, suspect_end = map(int, input().split())
    if check_alibi(crime_start, crime_end, suspect_start, suspect_end):
        print("Com alibi")
    else:
        print("Sem alibi")
