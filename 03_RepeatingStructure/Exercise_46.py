name = "."
total_leap = 0

while name != "":
    name = input("\nAthlete: ")
    if name != "":
        for c in range(1, 6):
            leap = float(input(f"{c}º leap: "))
            if ('high_score' not in vars()) or (leap > high_score):
                high_score = leap
            elif ('lower_score' not in vars()) or (leap < lower_score):
                lower_score = leap
            total_leap += leap
        print(f"\nBest leap: {high_score}")
        print(f"Worst leap: {lower_score}")
        average = (total_leap - high_score - lower_score) / 3
        print(f"Leap average: {round(average, 2)}")
        print("\n****Final result****")
        print(f"{name}: {round(average, 2)}")
