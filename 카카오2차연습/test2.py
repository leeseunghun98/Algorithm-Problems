import requests, json
from collections import deque

X_AUTH_TOKEN = 'a90b98f1c4ba1dc6bb45ef0b6097ae71'
baseURL = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
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

def locations_api(): # 현재 카카오 T 바이크 서비스 시각에 각 자전거 대여소가 보유한 자전거 수를 반환한다.
    return get_method("locations").get("locations", [])

def trucks_api():
    return get_method("trucks").get("trucks", [])

# key, value?, ID가 낮은 트럭의 명령부터 순서대로 처리, 자전거 상하차 명령무시시에도 6초소비
# 이동일 경우에 100m 추가, 서비스지역 벗어나는 명령 무시, 6초소비, 1분내에 할 수 있는 명령까지만 수행<- 명령최대10개
# 720번 호출
def simulate_api(moves): 
    return put_method("simulate", {"commands" : moves})

def score_api():
    return get_method("score")

# 분단위 소수점 없음, 분에만 대여요청, 자전거 대여소에 자전거가 없으면 요청 자동 취소
# 문제 목적 : 취소되는 요청 최소화, 트럭 이동 최소화
# 트럭 상하좌우만 이동, 오전10시에 ID0인 곳에 모여있고, 오후 10시까지 운행, 도중에 멈추는것도 가능, 한칸(100m) = 6초
# 자전거 하나를 싣고 내리는데 6초, 각 트럭 최대 20대

# 서버의 처리 순서
# 대여요청을 분마다 받음, 사용시간 다 된 자전거 반납 처리
# 대여요청 처리 : 자전거 1대 대여소에 2개 요청오면, 앞쪽에 위치한 요청에게 빌려주고 뒤는 취소

# problem 1 = 5 X 5, 분당 2건, 자전거 100대, 기존 각 대여소 자전거 4대, 트럭 5대
# problem 2 = 60 X 60, 분당 15건, 자전거 10800대, 기존 각 대여소 자전거 3대, 트럭 10대
# problem 2에서 과거 요청 기록 필요


# problem 1
problem = 1
N = 5
REQ_AVG = 2
BYCICLES = 100
TRUCKS = 5

# 반납 턴 후 대여 턴
TOKEN = start_api(1)
trucks = trucks_api()
OK = 3 - problem
locations = []

# 트럭의 움직임
dic = {1:[1,0], 2:[0,1], 3:[-1,0], 4:[0,-1]}

def bfs(t_location, x, y, t_id, loaded_bikes):
    r = t_location % 5
    c = t_location // 5
    dx = []
    dy = []
    dz = []
    # 방향
    if r > x: # 문제 기준 아래
        dx.append(-1)
        dy.append(0)
        dz.append(3)
    if r < x: # 문제 기준 위
        dx.append(1)
        dy.append(0)
        dz.append(1)
    if c > y: # 왼
        dx.append(0)
        dy.append(-1)
        dz.append(4)
    if c < y: # 오
        dx.append(0)
        dy.append(1)
        dz.append(2)
    mn_x = min(x, r); mx_x = max(x, r)
    mn_y = min(y, c); mx_y = max(y, c)
    dir = len(dx)
    queue = deque([[r, c, []]])
    while queue:
        j = queue.popleft()
        if len(j[-1]) >= 10 or (j[0] == x and j[1] == y):
            if len(j[-1]) < 10:
                # 5 자전거 상차, 6 자전거 하차
                j[-1] += [6]*(min(10 - len(j[-1]), j[-1].count(5) + loaded_bikes, 2))
            return j[-1]
        up = locations[j[0]*5+j[1]]["located_bikes_count"] - OK
        # 현재 위치 자전거 적당량 이상이면 트럭에 태우기
        if up > 0 and trucks[t_id]['loaded_bikes_count'] < 20: 
            j[-1] += [5]
        for i in range(dir):
            nx = j[0] + dx[i]
            ny = j[1] + dy[i]
            if (mn_x <= nx <= mx_x) and (mn_y <= ny <= mx_y):
                queue.append([nx, ny, j[-1] + [dz[i]]])

def call_trucks(x, y, using):
    li = []
    
    for truck in trucks:
        t_id = truck["id"]
        t_load_bikes = truck["loaded_bikes_count"]
        t_location = truck["location_id"]
        if using[t_id] == 0:
            a = t_location % 5
            b = t_location // 5
            li.append((t_id, t_load_bikes, t_location, abs(x-a) + abs(y-b)))
    li.sort(key = lambda x:x[3])
    for t_id, t_load_bikes, t_location, _ in li:
        if t_load_bikes >= 1: # 바이크 1개이상 있으면 선택
            j = bfs(t_location, x, y, t_id, t_load_bikes)
            return (t_id, j)
        j = bfs(t_location, x, y, t_id, t_load_bikes)
        if j.count(5) > 1:
            return (t_id, j)
    return (True, True)

def check_truck(t_id, moves):
    print(t_id, moves)
    for m in moves:
        if m < 5:
            r, c = dic[m]
            trucks[t_id]['location_id'] += r + c*5
        elif m == 5:
            trucks[t_id]['loaded_bikes_count'] += 1
        else:
            trucks[t_id]['loaded_bikes_count'] -= 1

for now in range(720):
    locations = locations_api()
    using_trucks = [0 for _ in range(TRUCKS)]
    truck = trucks_api()
    for location in locations:
        id = location["id"]
        bikes = location["located_bikes_count"]
        if bikes == 0:
            id, moves = call_trucks(id % 5, id // 5, using_trucks)
            print("id, move", id, moves)
            if id:
                continue
            if len(moves) > 10:
                moves = moves[:10]
            check_truck(id, moves)
            using_trucks[id] = moves
    commands = []
    for t_id, t_moves in enumerate(using_trucks):
        if t_moves != 0:
            commands.append({"truck_id":t_id, "command":t_moves})
    print(commands)
    print(simulate_api(commands))
    
print(score_api())
