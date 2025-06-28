
def get_user_guess():
    while True:
        try:
            Guess=int(input("Guess a number from 1-100:"))
            if 1<=Guess<=100:
                return Guess
            else:
                print("Please ener a number between 1-100.")
        except ValueError:
            print("invalid input! Please enter a number.")