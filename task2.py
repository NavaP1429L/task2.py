user_input = input("how much money are you saving per month?")
try:
    Usave = float(user_input)
    Yearsave = Usave * 12
    interestsave = Yearsave * 1.008
    if Yearsave.is_integer():
        print(int(Yearsave))
    else:
        print(f"{Yearsave:.2f}")
    print(f"£{interestsave:.2f}")
except ValueError:
    print("Invalid input")
