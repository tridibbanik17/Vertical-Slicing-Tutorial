import argparse
def main():
    # configure first call arg to be the price of the item
    parser = argparse.ArgumentParser()
    parser.add_argument("price", type=float, help="The price of the item")
    args  = parser.parse_args()
    price = args.price

    # Add tax to the price
    total = price * 1.13 # since in ON

    print(f"The total price is {total:.2f}")

if __name__ == '__main__':
    main()