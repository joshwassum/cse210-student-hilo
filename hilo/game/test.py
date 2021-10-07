import random
# dealer class

current_card = flip_card()


def flip_card():

    '''
    This function will return a new card from the deck list.
    '''

    return random.randint(1,13)




# user class


points = 300

def user_guess():

    guess = input("Will the next card be higher or lower than the current card? (h/l) ")
    return guess.strip().lower()


def apply_points():
    points = 300
    print(points)
    print(current_card)
    guess = user_guess()
    if guess == "h":
        if current_card < flip_card():
            print(current_card)
            points += 100
        elif current_card > flip_card():
            points -= 75
        else:
            print("draw")
    if guess == "l":
        if current_card > flip_card():
            points += 100
        elif current_card < flip_card():
            points -= 75
        else:
            print("draw")

    print(points)

