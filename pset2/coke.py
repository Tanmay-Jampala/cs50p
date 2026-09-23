PRICE = 50
ACCEPTED_COINS = [25, 10, 5]

def main():
    amount_paid = 0

    while amount_paid < PRICE:
        amount_due = PRICE - amount_paid
        print(f"Amount Due: {amount_due}")

        coin = int(input("Insert Coin: "))


        if coin in ACCEPTED_COINS:
            amount_paid += coin

    change_owed = amount_paid - PRICE
    print(f"Change Owed: {change_owed}")

main()