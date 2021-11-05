months = {
    '01': "January",
    '02': "February",
    '03': "March",
    '04': "April",
    '05': "May",
    '06': "June",
    '07': "July",
    '08': "August",
    '09': "September",
    '10': "October",
    '11': "November",
    '12': "December"
}


def convert_date(d, m, y):
    if m in months:
        print(f"{d} de {months[m]} de {y}")


dat = input("Type the date (dd/mm/yyyy): ")

day = dat[:2]
month = dat[3:5]
year = dat[6:]

convert_date(day, month, year)
