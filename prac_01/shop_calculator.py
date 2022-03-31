def main():
    total_price = 0
    num_item = int(input("Number of items: "))
    get_valid_num_item(num_item)
    get_items_price(num_item, total_price)


def get_valid_num_item(num_item):
    while num_item < 0:
        print("Invalid number")
        num_item = int(input("Number of items: "))


def get_items_price(num_item, total_price):
    for i in range(num_item):
        item_price = float(input("Price of item: "))
        total_price = item_price + total_price
    if total_price > 100:
        total_price = total_price * 0.9
    print(f"Total price for {num_item} items is $ {total_price:.2f}")


main()
