def get_valid_number(prompt, num_type):
    while True:
        try:
            return num_type(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a valid {num_type.__name__}.")

units_sold = get_valid_number("Enter the number of units sold: ", int)
price_per_unit = get_valid_number("Enter the price per unit: ", float)

total_revenue = units_sold * price_per_unit
print(f"Total revenue: ${total_revenue:.2f}")
