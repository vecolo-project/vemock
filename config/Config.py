class Config:
    def __init__(self, auto_off, max_seats, station_id,frequency_wait):
        self.auto_off = bool(auto_off)
        self.max_seats = int(max_seats)
        self.station_id = int(station_id)
        self.frequency_wait = float(frequency_wait)
