import requests, json

X_AUTH_TOKEN = '8adceec7af001258a52e7d00fd198604'
baseURL = "https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"
TOKEN = ""

def request(method, url, location, data={}, token="", init=False):
    headers = {'Content-Type' : "application/json"}
    if init is True:
        headers['X-Auth-Token'] = token
    else:
        headers['Authorization'] = token

    if method == "GET":
        res = requests.get(url+"/"+location, headers=headers)
    elif method == "POST":
        res = requests.post(url+"/"+location, headers=headers, json=data)
    elif method == "PUT":
        res = requests.put(url+"/"+location, headers=headers, json=data)

    # status_code = res.status_code
    # print(status_code)
    return res.json() 

get_method = lambda location : request("GET", baseURL, location, token=TOKEN)
post_method = lambda location, data : request("POST", baseURL, location, data=data, token=TOKEN)
put_method = lambda location, data : request("PUT", baseURL, location, data=data, token=TOKEN)

def start_api(problem_number):
    return request("POST", baseURL, "start", {'problem' : problem_number}, token=X_AUTH_TOKEN, init=True)['auth_key']

def score_api():
    return get_method("score")

def watingline_api(now):
    waits = get_method("waiting_line").get("waiting_line", [])
    return [[wait["id"], now - wait["from"]+1] for wait in waits]

def gameresult_api():
    results = get_method("game_result").get("game_result", [])
    return [[result["win"], result["lose"], result["taken"]] for result in results]

def userinfo_api():
    return get_method("user_info").get("user_info", [])

def match_api(data):
    return put_method("match", {"pairs" : data})

def changegrade_api(power):
    commands = [p for p in power]
    return put_method("change_grade", {"commands" : commands})

########### Get Token ############
# 매칭 신청 빈도 분당 평균 1건
# problem 만 changed
# problem = 2
# TOKEN = start_api(problem)
# print(TOKEN)
sco = []
for problem in [1, 2]:
    TOKEN = start_api(problem)
    POWER_MIN = 1000
    POWER_MAX = 100000
    POWER_AVG = 40000
    POWER_STD = 20000
    D = POWER_MAX - POWER_MIN
    num_users = len(userinfo_api())

    power = {}
    for id in range(1, num_users+1):
        power[id] = POWER_AVG

    def get_real_skill_diff(elapsed_time):
        return (40 - elapsed_time) * D / 35

    def get_reliability(win_power, lose_power, real_diff):
        return 1

    wait_weight = 2 + problem
    for now in range(595):
        game_result = gameresult_api()
        for win, lose, taken in game_result:
            estimate_diff = abs(power[win]-power[lose])  # 현재까지의 predict
            real_diff = get_real_skill_diff(taken)       # 게임 시간을 통해 얻은 ground_truth
            error_diff = estimate_diff-real_diff           # error: predict - ground_truth
            prob = get_reliability(power[win], power[lose], real_diff)  # 추정 신뢰도
            update_value = error_diff * prob / 2           # error에 추정 신뢰도 곱해 반영값 생성 (win과 lose 각각 반영할 것이므로 2로 나눔)
            power[win] = max(POWER_MIN, power[win]-update_value)
            power[lose] = min(POWER_MAX, power[lose]+update_value)

        waitings = watingline_api(now)
        waitings.sort(reverse=True)

        match_list = []
        i = 0
        while i+1 < len(waitings):
            # 대기시간에 따른 가중치
            # 0~15분을 wait_weight개의 구역으로 구분해 나눔
            diff = (power[waitings[i][0]] - power[waitings[i+1][0]]) / ((waitings[i][1] + waitings[i+1][1])//2//wait_weight+1)
            if diff <= 20000:  # matching 성공
                match_list.append([waitings[i][0], waitings[i+1][0]])
                i += 2
            else:  # matching 실패
                i += 1
        print(match_api(match_list))

    changegrade_api(power)
    print(match_api([]))
    sco.append(score_api())
for s in sco:
    print(s)
