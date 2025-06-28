import random
responses=["Yes,definitly!","No,not now.","Ask again later","It is certain","Very doubtful","Outlook is good","Better not tell you now","Concentrate and ask again"]
def get_random_response():
    return random.choice(responses)

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