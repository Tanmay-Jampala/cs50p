

MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

MAX_DAY = 31


def main():
    while True:
        date = input("Date: ").strip()

        parsed = parse_slashes(date)
        if parsed is None:
            parsed = parse_words(date)

        if parsed is not None:
            month, day, year = parsed
            print(f"{year}-{month:02}-{day:02}")
            return


def parse_slashes(date):
    parts = date.split("/")

    if len(parts) != 3:
        return None

    try:
        month, day, year = [int(part) for part in parts]
    except ValueError:
        return None

    return validated(month, day, year)


def parse_words(date):
    month_and_day, comma, year = date.partition(",")

    if not comma:
        return None

    parts = month_and_day.split()

    if len(parts) != 2:
        return None

    month_name, day = parts

    if month_name not in MONTHS:
        return None

    try:
        month = MONTHS.index(month_name) + 1
        return validated(month, int(day), int(year))
    except ValueError:
        return None


def validated(month, day, year):
    if 1 <= month <= 12 and 1 <= day <= MAX_DAY and year >= 1:
        return month, day, year

    return None


main()
