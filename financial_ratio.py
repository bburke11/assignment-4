while True:
    try:
        profit = float(input("Enter profit: "))
        revenue = float(input("Enter revenue: "))
        ratio = profit / revenue
    except ValueError:
        pass
    except ZeroDivisionError:
        print("Revenue cannot be zero. Please try again.")
    else:
        print(f"Profit margin ratio: {ratio * 100:.2f}%")
        break
