# import requests
# import httpx
import http.client
import json


def submit_state(api_endpoint, state, jwt_token, debug=True):
    headers = {'Authorization': 'Bearer ' + jwt_token, 'Content-type': 'application/json'}
    data = {
        'battery': state.battery,
        'charging_power': state.charging_power,
        'active': state.active,
        'used_seats': state.used_seats,
    }
    conn = http.client.HTTPSConnection(api_endpoint)
    conn.request('POST', '', json.dumps(data), headers)
    if debug:
        print(conn.getresponse().read().decode())
    # print(response.read().decode())
    # response = requests.post(api_endpoint, headers=headers, json=data)
    #     print('url : ' + response.request.url)
    #     print('headers : ', response.request.headers)
    #     print('body : ', response.request.body)
