#Reads a fuel gauge fraction like 3/4 and reports how full the tank is.


def main():
    percentage = get_percentage()
    print(format_gauge(percentage))


def get_percentage():
    while True:
        fraction = input("Fraction: ")

        try:
            numerator, denominator = fraction.split("/")
            fuel = int(numerator) / int(denominator)
            percentage = round(fuel*100)
        except (ValueError, ZeroDivisionError):
            continue

        if not 0<= fuel <= 1:
            continue

        return round(fuel*100)

def format_gauge(percentage):
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"

    return f"{percentage}%"

main()