import datetime
import pytz


def turn_date_into_string(date: datetime) -> str:
    return date.strftime('%d/%m/%Y %H:%M')


def turn_dt_to_string(delta: datetime.timedelta) -> str:
    days = delta.days
    minutes = delta.seconds // 60
    if delta > datetime.timedelta(0):
        if days == 0:
            return f'{minutes} minutes'
        elif minutes == 0:
            return f'{days}'
        else:
            return f'{days} jours, {minutes} minutes'

    if delta < datetime.timedelta(0):
        days = -days
        minutes = minutes
        if days == 0:
            return f'{minutes} minutes'
        elif minutes == 0:
            return f'{days}'
        else:
            return f'{days} jours, {minutes} minutes'

if __name__ == '__main__':
    d1 = datetime.datetime.strptime('27/3/2023 7h50', '%d/%m/%Y %Hh%M')
    d2 = datetime.datetime.strptime('27/3/2023 14h50', '%d/%m/%Y %Hh%M')
    print(turn_date_into_string(d1), turn_date_into_string(d2),turn_dt_to_string(d2-d1))

    euro = pytz.timezone('Europe/Paris')
    asia = pytz.timezone('Asia/Macao')

    d1_ = euro.localize(d1)
    d2_ = asia.localize(d2)
    print(turn_date_into_string(d1_), turn_date_into_string(d2_), turn_dt_to_string(d2_-d1_))