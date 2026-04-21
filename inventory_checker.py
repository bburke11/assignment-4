def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")

inventory = get_valid_int("Enter the current inventory level: ")
threshold = get_valid_int("Enter the minimum reorder threshold: ")

try:
    percentage = (inventory / threshold) * 100
    print(f"Inventory is at {percentage:.1f}% of the reorder threshold.")
except ZeroDivisionError:
    print("Error: Threshold cannot be zero. Cannot calculate percentage.")

if inventory < threshold:
    print(f"REORDER ALERT: Inventory ({inventory}) is below the threshold ({threshold}).")
else:
    print(f"Inventory level is sufficient ({inventory} units).")
