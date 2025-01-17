import argparse

def main():
    # Configure CLI arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("price", type=float, help="The price of the item")
    parser.add_argument(
        "province",
        type=str,
        choices=["Ontario", "Quebec"],
        help="The province where the tax is applied"
    )
    parser.add_argument(
        "discount",
        type=float,
        default=0,
        help="The discount percentage (0.03, 0.05, 0.07, 0.10, or 0.15)"
    )
    args = parser.parse_args()

    # Add sales discounts based on specific price thresholds
    print("Discount can be applied only to purchases of 1k, 5k, 7k, 10k, or 50k dollars.")
    if args.price == 1000:
        args.discount = 0.03
        print("The discount to be added is 3%.")
    elif args.price == 5000:
        args.discount = 0.05
        print("The discount to be added is 5%.")
    elif args.price == 7000:
        args.discount = 0.07
        print("The discount to be added is 7%.")
    elif args.price == 10000:
        args.discount = 0.10
        print("The discount to be added is 10%.")
    elif args.price == 50000:
        args.discount = 0.15
        print("The discount to be added is 15%.")
    else:
        print("No discount applicable for the given price.")

    # Apply the discount if applicable
    if args.discount > 0:
        args.price -= args.price * args.discount
        print(f"After applying the discount, the price is reduced to {args.price:.2f}")

    # Set the tax rate based on the province
    if args.province == "Ontario":
        tax_rate = 1.13  # Ontario's tax rate
    elif args.province == "Quebec":
        tax_rate = 1.14975  # Quebec's tax rate

    # Calculate the total price with tax
    total = args.price * tax_rate
    print(f"The total price after adding the discount and tax in {args.province} is {total:.2f}")

if __name__ == '__main__':
    main()
