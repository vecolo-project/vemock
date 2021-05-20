from datetime import datetime


def is_day():
    return 8 <= datetime.now().hour <= 19


def is_morning():
    return 8 <= datetime.now().hour <= 12


def is_middle_day():
    return 12 <= datetime.now().hour <= 15


def is_afternoon():
    return 15 <= datetime.now().hour <= 19
