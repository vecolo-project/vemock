import json


def add_stations(station_list, config, fp):
    for station in station_list:
        fp.write(f'''
  vemock_station_{station['station_id']}:
    environment:
      - station_id={station['station_id']}
      - auto_off={station['auto_off']}
      - max_seats={station['max_seats']}
      - history_path={config['history_path']}
      - frequency_wait={config['frequency_wait']}
      - max_charge={station['max_charge']}
      - jwt_token={station['jwt_token']}
      - api_endpoint={config['api_endpoint']}
    volumes:
      - vemock_station_{station['station_id']}:/usr/src/app/history
    networks:
      - vemock_network
    restart: unless-stopped
    logging:
      driver: "json-file"
      options:
        max-size: "{config['max_log_size']}"
        max-file: "{config['max_log_file']}"
    image: vemock''')


def add_volumes(station_list, fp):
    fp.write('\nvolumes:')
    for station in station_list:
        fp.write(f'''
  vemock_station_{station['station_id']}:
    driver: local''')


def get_json(filename):
    with open(filename, 'r') as fp:
        return json.load(fp)


with open("docker-compose.yml", 'w') as file_p:
    config_json = get_json("config.json")
    file_p.write('''version: '3.8'
services:''')
    add_stations(config_json['station_list'], config_json['config'], file_p)
    add_volumes(config_json['station_list'], file_p)
    file_p.write('''
networks:
  vemock_network:
    name: vemock_network
    driver: overlay
    attachable: true''')
