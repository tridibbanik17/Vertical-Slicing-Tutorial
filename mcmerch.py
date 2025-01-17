import argparse
def main():
    # configure CLI arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("price", type=float, help="The price of the item")
    parser.add_argument(
        "province",
        type=str,
        default="Ontario",
        choices=["Ontario", "Quebec"],
        help="The province where the tax is applied (default: Ontario)"
    )
    args  = parser.parse_args()

    # Set the tax rate based on the province
    if args.province == "Ontario":
        tax_rate = 1.13 # Ontario's tax rate
    
    elif args.province == "Quebec":
        tax_rate = 1.14975 # Quebec's tax rate 

    # Calculate the total price with tax
    total = args.price * tax_rate 

    print(f"The total price in {args.province} is {total:.2f}")

    #     # Add sales discounts on 1k, 5k, 7k 10k and 50k dollars of purchase
    # print("Discount can be added only to 1k, 5k, 7k 10k and 50k dollars of purchases")
    # if price == 1000:
    #     print("The discount to be added is 3%.")
    #     price = price - price*0.03
    #     print(f"After adding the discount, the price is reduced to {price}")

    # elif price == 5000:
    #     print("The discount to be added is 5%.")
    #     price = price - price*0.05
    #     print(f"After adding the discount, the price is reduced to {price}")

    # elif price == 7000:
    #     print("The discount to be added is 7%.")
    #     price = price - price*0.07
    #     print(f"After adding the discount, the price is reduced to {price}")

    # elif price == 10000:
    #     print("The discount to be added is 10%.")
    #     price = price - price*0.10
    #     print(f"After adding the discount, the price is reduced to {price}")
        
    # elif price == 50000:
    #     print("The discount to be added is 15%.")
    #     price = price - price*0.15
    #     print(f"After adding the discount, the price is reduced to {price}")

if __name__ == '__main__':
    main()
