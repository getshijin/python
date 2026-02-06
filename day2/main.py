if __name__ == "__main__":
    print("Welcome to tip calculator!")
    bill_amount = int(input("What was the total bill? $"))
    per_split = int(input("how much tip you want to give 10,12 or 15 % "))
    per_count = int(input("How many people to split the bill? "))
    print(f"Each person should pay: ${ (bill_amount+(bill_amount* (per_split/100)))/per_count }")
