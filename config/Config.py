import distutils.util


class Config:
    def __init__(self, auto_off, max_seats, station_id, frequency_wait, history_path, jwt_token, api_endpoint,
                 max_charge, debug):
        self.auto_off = bool(distutils.util.strtobool(auto_off))
        self.max_seats = int(max_seats)
        self.station_id = int(station_id)
        self.frequency_wait = float(frequency_wait)
        self.history_path = str(history_path)
        self.jwt_token = str(jwt_token)
        self.api_endpoint = str(api_endpoint)
        self.max_charge = float(max_charge)
        self.debug = bool(distutils.util.strtobool(debug))
