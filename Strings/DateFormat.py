def date_validity(day):
    dd = int(day[:2])
    mm = int(day[3:5])
    yy = int(day[6:])

    if(dd > 31 or dd < 1):
        print("Bad day")
        return False
    elif (mm > 12 or mm < 1):
        print("Bad month")
        return False
    elif((yy) > 10000 or (yy < 1000)):
        print("Bad year")
        return False
    return True

def check_hour(hour):
    hh = int(hour[:2])
    mm = int(hour[3:5])
    ss = int(hour[6:])

    if(hh > 24 or hh < 0):
        print("Bad hours")
        return False
    elif (mm > 60 or mm < 0):
        print("Bad minutes")
        return False
    elif (ss > 60 or ss < 0):
        print("Bad seconds")
        return False
    return True

def checkDate(date):
    day = date[:10]
    hour = date[11:]

    if(date_validity(day) and check_hour(hour)):
        return True
    return False


def main():
    date = input("Enter a date")
    print(checkDate(date))


main()