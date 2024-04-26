import datetime
import locale

locale.setlocale(locale.LC_ALL, 'usa')

if __name__ == "__main__":
    file = open("contract_dates.txt")
    content = file.readlines()
    s1 = content[0]
    s2 = content[1]
    s1 = s1.removeprefix("Purchase: ")
    s2 = s2.removeprefix("Repair: ")

    s1_split = s1.split(",")
    s2_split = s2.split(";")

    print(s1_split[0], s1_split[1])
    print(s2_split[0], s2_split[1])

    purchase_date = datetime.datetime.strptime(s1_split[0], "%d/%m/%y %Hh%M")
    repair_date_start = datetime.datetime.strptime(s2_split[0], "%Y-%m-%d %H:%M%p")
    repair_date_end = datetime.datetime.strptime(s2_split[1], "%Y-%m-%d %H:%M%p")
    guarantee_duration = datetime.timedelta(int(s1_split[1].split(" ")[1]))
    repair_duration = repair_date_end - repair_date_start
    end_guarantee_date = purchase_date + guarantee_duration
    str_end_guarantee_date = end_guarantee_date.strftime("le %A %b %Y à %Hh%m")

    print(f"Purchase weekday : {purchase_date.strftime("%A")}")

    reference_date = datetime.datetime(year=2024, month=1, day=1, hour=12)

    locale.setlocale(locale.LC_ALL, 'fr_FR')
    end_guarantee_date = end_guarantee_date + repair_duration

    if end_guarantee_date > reference_date:
        print(f"Votre garantie a été prolongée, elle expirera {str_end_guarantee_date}")

    if datetime.datetime.now() > end_guarantee_date:
        print(f"Votre garantie est échue")
    else:
        print(f"Votre garantie est valable")
