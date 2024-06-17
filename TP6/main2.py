import locale
from datetime import datetime, timedelta
locale.setlocale(locale.LC_TIME, 'en_US')

if __name__ == "__main__":
    with open("contract_dates.txt", "r") as f:
        content = f.read()
        data = content.split("\n")

        s1 = data[0].split(",")
        s2 = data[1].split(";")
        s1 = [x.removeprefix("Purchase: ") for x in s1]
        s1 = [x.removesuffix(" jours") for x in s1]
        s1 = [x.removesuffix(" ") for x in s1]
        s2 = [x.removeprefix("Repair: ") for x in s2]
        print(s1)
        print(s2)

    purchase_date = datetime.strptime(s1[0], "%d/%m/%y %Hh%M")
    warranty_dt = timedelta(days=int(s1[1]))
    purchase_day = purchase_date.strftime("%A")

    print(purchase_day)

    begin_repair_date = datetime.strptime(s2[0], "%Y-%m-%d %H:%Mpm")
    end_repair_date = datetime.strptime(s2[1], "%Y-%m-%d %H:%Mpm")
    dt_repair = end_repair_date - begin_repair_date

    final_warranty_date = purchase_date + warranty_dt + dt_repair

    print(f"Votre garantie a été prolongée, elle expirera le {final_warranty_date.strftime('%A %d %B %Y à %Hh%M')}")

    print("La garantie n'est plus valide") if datetime.now() > final_warranty_date else print("La garantie est toujours valide!")