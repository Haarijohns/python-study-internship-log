while True:

    try:
        duration = int(input("How many minutes did you study? "))

        if duration <= 0:
            print("Enter a valid duration.")
            continue

        print(f"You studied for {duration} minutes.")
        break

    except ValueError:
        print("Invalid input! Please enter a whole number.")
