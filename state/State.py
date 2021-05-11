import datetime
import random


def is_day():
    return 8 <= datetime.datetime.now().hour <= 19


def is_morning():
    return 8 <= datetime.datetime.now().hour <= 12


def is_middle_day():
    return 11 <= datetime.datetime.now().hour <= 15


def is_afternoon():
    return 12 <= datetime.datetime.now().hour <= 19


class State:
    def __init__(self, battery, auto_off, used_seats, max_seats, charging_power=0.0, max_charging_power=20.0,
                 active=True):
        self.battery = float(battery)
        self.auto_off = bool(auto_off)
        self.used_seats = int(used_seats)
        self.max_seats = int(max_seats)
        self.charging_power = float(charging_power)
        self.max_charging_power = float(max_charging_power)
        self.active = bool(active)

    def next_state(self):
        self.next_state_discharge()
        self.next_state_active()
        self.next_state_charge()
        self.next_state_seats()

    def next_state_discharge(self):
        # Elle se décharge régulièrement, un peu moins la nuit (vu que moins d'utilisation)
        if is_day():
            # Se décharge plus vite si il y a beaucoup de vélos sur la borne
            discharge = 0.001 * self.used_seats
        else:
            discharge = 0.0002 * self.used_seats
        # Le random va tourner plus en faveur du chargement de la batterie si < 15%
        if self.battery > 15:
            discharge += round(random.uniform(0.000, 0.010), 3)

        # La batterie ne doit pas dépasser 100% et descendre en dessous de 0
        self.battery = min(100., max(0., float("{:.4f}".format(self.battery - discharge))))

    def next_state_active(self):
        if self.auto_off:
            if self.active:
                self.active = self.battery >= 10
            else:
                self.active = self.battery >= 15

    def next_state_charge(self):
        # Elle se décharge régulièrement, un peu moins la nuit (vu que moins d'utilisation)
        if is_day():
            random_charge = \
                random.uniform(-self.max_charging_power / 50, self.max_charging_power / 20) \
                    if is_middle_day() \
                    else random.uniform(-self.max_charging_power / 50, self.max_charging_power / 50) \
                    if is_morning() \
                    else random.uniform(-self.max_charging_power / 50, self.max_charging_power / 40)

            self.charging_power = min(self.max_charging_power,
                                      max(0., float("{:.4f}".format(self.charging_power + random_charge))))
        else:
            self.charging_power = max(0., float("{:.4f}".format(self.charging_power - 0.1)))

        self.battery = min(100.,
                           max(0., float("{:.4f}".format(
                               self.battery + (self.charging_power / 20000)))))

    def next_state_seats(self):
        randmax = 10 if is_day() else 50
        if self.used_seats > 0:
            if random.randint(0, randmax) == randmax:
                self.used_seats -= 1
        if self.used_seats < self.max_seats:
            if random.randint(0, randmax) == randmax:
                self.used_seats += 1