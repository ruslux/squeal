from datetime import datetime, timedelta
from decimal import Decimal, ROUND_HALF_UP
import re


def parse_overtime(message_text):
    date_regexp = r'^((вчера|(\d{4}-)?((0?\d|1[0-2])-)?((0?|[12])\d|3[01]))\n)?'
    time_array_regexp = r'(с ([0-2]?\d)(:[0-5]\d)?)?( ?до ([0-2]?\d)(:[0-5]\d)?)?'
    hours_regexp = r'(\n({}|\d+(\.5)?))?$'.format(time_array_regexp)

    if not re.search(date_regexp + r'.+' + hours_regexp, message_text, re.IGNORECASE):
        return False

    now = datetime.now()

    date = specified_date = re.findall(date_regexp, message_text, re.IGNORECASE)[0][1]
    task = message_text.split('\n')[bool(date)]
    hours = re.findall(hours_regexp, message_text, re.IGNORECASE)[0][1]

    if date == '':
        date = str(now)[:10]
    elif date.lower() == 'вчера':
        date = str(now - timedelta(days=1))[:10]

    if not re.search(r'^\d+(\.5)$', hours, re.IGNORECASE):
        additional_days = 0
        time_array = re.findall(time_array_regexp, hours, re.IGNORECASE)[0]
        time_array = [
            time_array[1],
            time_array[2][1:],
            time_array[4],
            time_array[5][1:]
        ]
        if not time_array[0]:
            time_array[0] = '19'  # TODO: take from database
        if not time_array[1]:
            time_array[1] = '00'
        if not time_array[2]:
            time_array[2] = str(now)[11:13]
            time_array[3] = str(now)[14:16]
            additional_days = (datetime.strptime(str(now)[:10], '%Y-%m-%d') - datetime.strptime(date, '%Y-%m-%d')).days
        if not time_array[3]:
            time_array[3] = '00'
        start = datetime.strptime('{}T{}:{}'.format(date, time_array[0], time_array[1]), '%Y-%m-%dT%H:%M')
        finish = datetime.strptime('{}T{}:{}'.format(date, time_array[2], time_array[3]), '%Y-%m-%dT%H:%M')
        finish += timedelta(days=additional_days)
        if start > finish:
            if not specified_date:
                date = str(now - timedelta(days=1))[:10]
                start -= timedelta(days=1)
            else:
                return False
        hours = int(Decimal(int((finish - start).total_seconds()) / (3600 / 2)).quantize(0, ROUND_HALF_UP)) / 2

    return {'date': date, 'task': task, 'hours': float(hours)}
