def main():
    total = 0
    items_number = int(input("Number of items: "))
    while items_number < 0:
        print("invalid number of items!")
        items_number = int(input("Number of items: "))

    for i in range(items_number):
        items_price = float(input("Price of item: "))
        total = total + items_price

    if total > 100:
        discounted = total - (total * 0.1)
        print("Total price for {} items is ${:.2f}".format(items_number, discounted))
    else:
        print("Total price for {} items is ${:.2f}".format(items_number, total))


if __name__ == '__main__':
    main()
