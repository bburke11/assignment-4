# PROMOTION_NAME = "Summer Sale"  # Commented out to simulate NameError

def get_customer_age():
    while True:
        try:
            age = int(input("Enter customer age: "))
            if age <= 0:
                print("Age must be a positive integer. Please try again.")
                continue
            return age
        except ValueError:
            print("Invalid input. Please enter a whole number.")

age = get_customer_age()

try:
    print(f"Promotion: {PROMOTION_NAME}")
except NameError:
    print("Notice: Promotion name is not defined (NameError caught).")

if age >= 18:
    print(f"Customer (age {age}) is eligible for age-restricted promotions.")
else:
    print(f"Customer (age {age}) is not eligible for age-restricted promotions.")
