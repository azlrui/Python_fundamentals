from datetime import datetime, timedelta
import pytz


def throw_str_datetime(date : datetime):
    return date.strftime("%d/%m/%Y %H:%M")

def throw_str_timedelta(delta : timedelta):
    delta = delta if delta >= timedelta(0) else -delta
    jours = delta.days
    minutes = delta.seconds / 60
    heures = minutes / 60
    return f"{jours} jours, {minutes} minutes"

if __name__ == "__main__":
    d1 = datetime.strptime("27/03/2023 07h50", "%d/%m/%Y %Hh%M")
    d2 = datetime.strptime("27/03/2023 14h50", "%d/%m/%Y %Hh%M")

    print(throw_str_datetime(d1), throw_str_datetime(d2))
    print(throw_str_timedelta(d1-d2))

    europe = pytz.timezone('Europe/Paris')
    asie = pytz.timezone('Asia/Macao')

    d1 = europe.localize(d1)
    d2 = asie.localize(d2)
    print(throw_str_timedelta(d1-d2))
