def main():
    dollars=dollars_to_float(input("How much was the meal?"))
    percent=percent_to_float(input("What percentage would you like to tip?"))
    tip=dollars*percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    dollars = d.replace("$", "")
    number = float(dollars)
    return number

def percent_to_float(p):
    percent = p.replace("%", "")
    number = float(percent) / 100
    return number

main()