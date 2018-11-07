import re

CITY_NUMBER = r'\d' \
              r'(-?\d){1,6}'

FEDERAL_NUMBER = r'((\+?7)?(\(\d{3}\)-?)|((^|(\+?7-))\d{3}-)|((\+?7)?\d{3}))' \
                 r'\d(-?\d){6}'


def is_city_number(s):
    res = re.match(CITY_NUMBER, s)
    return res is not None and len(res.group(0)) == len(s)


def is_federal_number(s):
    res = re.match(FEDERAL_NUMBER, s)
    return res is not None and len(res.group(0)) == len(s)


def is_phone_number(s):
    if is_city_number(s):
        return 'city'
    if is_federal_number(s):
        return 'federal'
    return False
