import random

from time_helper.functions import is_day, is_middle_day, is_morning


class State:
    def __init__(self, battery, auto_off, used_seats, max_seats, max_charging_power=20.0,
                 active=True, charging_power=0.0):
        self.battery = float(battery)
        self.auto_off = bool(auto_off)
        self.used_seats = int(used_seats)
        self.max_seats = int(max_seats)
        self.charging_power = float(charging_power)
        self.max_charging_power = float(max_charging_power)
        self.active = bool(active)

    def next_state(self, frequency_wait):
        self.next_state_discharge(frequency_wait)
        self.next_state_charge(frequency_wait)
        self.next_state_active()
        self.next_state_seats(frequency_wait)

    def next_state_discharge(self, frequency_wait):
        # Elle se décharge régulièrement, un peu moins la nuit (vu que moins d'utilisation)
        if is_day():
            # Se décharge plus vite si il y a beaucoup de vélos sur la borne
            discharge = 0.0005 * self.used_seats * frequency_wait
        else:
            discharge = 0.0002 * self.used_seats * frequency_wait
        # Le random va tourner plus en faveur du chargement de la batterie si < 15%
        if self.battery > 15:
            discharge += float("{:.4f}".format(random.uniform(0.000, 0.0005 * frequency_wait)))
            # La batterie ne doit pas dépasser 100% et descendre en dessous de 0
            self.battery = min(100., max(0., float("{:.4f}".format(self.battery - discharge))))
        else:
            self.battery = min(100., max(0., float("{:.4f}".format(self.battery - (discharge / 2)))))

    def next_state_active(self):
        if self.auto_off:
            if self.active:
                self.active = self.battery >= 10
            else:
                self.active = self.battery >= 15

    def next_state_charge(self, frequency_wait):
        # Elle se décharge régulièrement, un peu moins la nuit (vu que moins d'utilisation)
        if is_day():
            random_charge = \
                random.uniform(0, (self.max_charging_power * frequency_wait) / 10) \
                    if is_middle_day() \
                    else random.uniform(-(self.max_charging_power * frequency_wait) / 50,
                                        (self.max_charging_power * frequency_wait) / 20) \
                    if is_morning() \
                    else random.uniform(-(self.max_charging_power * frequency_wait) / 50,
                                        (self.max_charging_power * frequency_wait) / 30)

            self.charging_power = min(self.max_charging_power,
                                      max(0., float("{:.4f}".format(self.charging_power + random_charge))))
        else:
            self.charging_power = max(0., float("{:.4f}".format(self.charging_power - (0.03 * frequency_wait))))

        self.battery = min(100.,
                           max(0., float("{:.4f}".format(
                               self.battery + (self.charging_power / 1000)))))

    def next_state_seats(self, frequency_wait):
        randmax = round(15 / frequency_wait) if is_day() else round(65 / frequency_wait)
        if self.used_seats > 0:
            if random.randint(0, randmax) == randmax:
                self.used_seats -= 1
        if self.used_seats < self.max_seats:
            if random.randint(0, randmax) == randmax:
                self.used_seats += 1
