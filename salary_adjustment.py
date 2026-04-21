def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    salary = get_valid_float("Enter current salary: ")

    while True:
        adjustment = get_valid_float("Enter adjustment percentage (0-100): ")
        if adjustment < 0:
            print("Adjustment percentage cannot be negative. Please try again.")
        elif adjustment > 100:
            print("Adjustment percentage cannot exceed 100. Please try again.")
        else:
            break

    new_salary = salary * (1 + adjustment / 100)
    print(f"Original salary: ${salary:,.2f}")
    print(f"Adjustment: {adjustment:.1f}%")
    print(f"New salary: ${new_salary:,.2f}")

main()
