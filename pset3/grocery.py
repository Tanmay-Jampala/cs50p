def main():
    grocery_list = {}

    while True:
        try:
            item = input().strip().lower()
        except EOFError:
            print()
            break

        if item:
            grocery_list[item] = grocery_list.get(item, 0) + 1

    for item in sorted(grocery_list):
        print(grocery_list[item], item.upper())

main()