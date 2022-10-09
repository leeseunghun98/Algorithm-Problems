import json, requests

AUTH_KEY = 'ab9056f8-5234-4683-959c-8d01e0c3b842'

baseURL = "https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"

def waitingline_api(auth_key):
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    url = baseURL + '/waiting_line'
    response = requests.get(url, headers = headers)
    return response.json()

print(waitingline_api(AUTH_KEY))