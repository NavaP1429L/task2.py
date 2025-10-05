try:
    Usave = float(input("How much money are you saving per month? "))
    Yearsave = Usave * 12
    interestsave = Yearsave * 1.008  # 0.8% interest
    print(f"Total savings for the year: £{Yearsave:.2f}")
    print(f"Total with interest: £{interestsave:.2f}")
except ValueError:
    print("Please enter a valid number.")
