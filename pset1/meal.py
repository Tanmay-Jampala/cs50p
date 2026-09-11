def main():
    time = input("Enter the time in HH:MM format: ")
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    total_minutes = hours * 60 + minutes
    if 7 * 60 <= total_minutes < 9 * 60:
        print("breakfast time")
    elif 12 * 60 <= total_minutes < 14 * 60:
        print("lunch time")
    elif 18 * 60 <= total_minutes < 20 * 60:
        print("dinner time")
main()