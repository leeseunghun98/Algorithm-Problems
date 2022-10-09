import json, requests
X_AUTH_TOKEN = 'da62d9728d50b07af6cc5ce9c61c389a'
baseURL = "https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"

def start_api(auth_key):
    headers = {'X-Auth-Token': auth_key, 'Content-Type': 'application/json'}
    url = baseURL + '/start'
    params = {'problem':1}
    response = requests.post(url, headers = headers, params=params)
    return response.json()
# AUTH_KEY = start_api(X_AUTH_TOKEN)['auth_key']
# print(AUTH_KEY)
AUTH_KEY = '7e901a6c-2904-42b1-8f6f-49c2c5ac52e7'
baseURL = "https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"

def userinfo_api(auth_key):
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    url = baseURL + '/user_info'
    response = requests.get(url, headers = headers)
    return response.json()

def waitingline_api(auth_key):
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    url = baseURL + '/waiting_line'
    response = requests.get(url, headers = headers)
    return response.json()

def gameresult_api(auth_key):
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    url = baseURL + '/game_result'
    response = requests.get(url, headers = headers)
    return response.json()

def match_api(auth_key, match):
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    data = {'pairs' : match}
    url = baseURL + '/match'
    response = requests.put(url, headers = headers, data = json.dumps(data))
    return response.json()

def changegrade_api(auth_key, grades):
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    data = {'commands' : grades}
    url = baseURL + '/change_grade'
    response = requests.put(url, headers = headers, data = json.dumps(data))
    return response.json()



print(userinfo_api(AUTH_KEY))

print(waitingline_api(AUTH_KEY))

print(gameresult_api(AUTH_KEY))
print(match_api(AUTH_KEY, [[1, 1], [9, 7], [11, 49]]))


# print(changegrade_api(AUTH_KEY, [{"id" : 1, "grade": 1900}]))











#### Get Score
# def score_api(auth_key):
#     headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
#     url = baseURL + '/score'
#     response = requests.get(url, headers = headers)
#     return response.json()

# print(score_api(AUTH_KEY))