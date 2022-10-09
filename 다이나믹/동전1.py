def solution(play_time, adv_time, logs):
    answer = ''
    
    def get_time(s):
        return int(s[:2])*3600 + int(s[3:5])*60 + int(s[-2:])
    
    play_time = get_time(play_time)
    adv_time = get_time(adv_time)
    
    dp = [0 for _ in range(play_time+1)]
    for l in logs:
        a, b = l.split("-")
        a = get_time(a)
        b = get_time(b)
        dp[a] += 1
        dp[b] -= 1
    for i in range(play_time):
        dp[i+1] = dp[i]
    for i in range(play_time):
        dp[i+1] = dp[i]
    ans = 0
    for i in range(adv_time, play_time+1):
        tmp = dp[i] - dp[i - adv_time]
        if tmp > ans:
            ans = tmp
            answer = i
    
    answer = str(answer // 3600).zfill(2) + ":" + str((answer % 3600) // 60).zfill(2) + ":" + str((answer % 3600) % 60).zfill(2)
    
    return answer

play_time = input()[1:-1]
adv_time = input()[1:-1]
logs = list(input()[1:-1].split(","))
print(logs)
for i in range(len(logs)):
    logs[i] = logs[i][1:-1]
print(logs)
solution(play_time, adv_time, logs)
