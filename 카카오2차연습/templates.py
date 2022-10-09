import requests, json

X_AUTH_TOKEN = ''
baseURL = ""
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