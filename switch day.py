import datetime

def find_day():
    day = datetime.datetime.today().weekday()

    if day == 0:
        return "Today is Monday"
    elif day == 1:
        return "Today is Tuesday"
    elif day == 2:
        return "Today is Wednesday"
    elif day == 3:
        return "Today is Thursday"
    elif day == 4:
        return "Today is Friday"
    elif day == 5:
        return "Today is Saturday"
    elif day == 6:
        return "Today is Sunday"

print(find_day())