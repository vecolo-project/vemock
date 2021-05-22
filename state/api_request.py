import requests


def submit_state(api_endpoint, state, jwt_token, debug=True):
    headers = {'Authorization': 'Bearer ' + jwt_token}
    data = {
        'battery': state.battery,
        'charging_power': state.charging_power,
        'active': state.active,
        'used_seats': state.used_seats,
    }
    response = requests.post(api_endpoint, headers=headers, json=data)
    if debug:
        print('url : ' + response.request.url)
        print('headers : ', response.request.headers)
        print('body : ', response.request.body)
