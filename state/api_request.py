import json

import requests


def submit_state(api_endpoint, state, jwt_token):
    headers = {'Authorization': 'Bearer ' + jwt_token}
    data = state.__dict__
    response = requests.post(api_endpoint, headers=headers, json=data)
    print('url : ' + response.request.url)
    print('headers : ', response.request.headers)
    print('body : ', response.request.body)
