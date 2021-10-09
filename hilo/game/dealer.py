from game.deck import Deck


class Dealer:

    '''
    Attributes:
    call the deck class
    continue playing?
    total points
    '''

    def __init__(self):
        """The class constructor.
        builds deck, sets the keep_playing to true, sets the total points equal 300.

        Arg: self(Dealer): an instance of dealer
        """

        self.deck = Deck()
        self.keep_playing = True
        self.total_points = 300

    def start_game(self):
        '''
        Shuffles the deck.
        Starts game loop.
        gets card for dealer, user guesses hi or low, then it caculate the points, asks 
        to play again, if the deck gets to the last card it will shuffle the deck again.

          Arg: self(Dealer): an instance of dealer
        '''
        self.deck.shuffle()
        while self.keep_playing:
            dealers_card = self.deal_cards()
            user_guess = self.guess_hi_low(dealers_card)
            self.calculate_points(user_guess, dealers_card)
            self.keep_playing = self.another_round()
            if len(self.deck.all_cards) <= 1:
                self.deck = Deck()
                self.deck.shuffle()

    def guess_hi_low(self, dealers_card):
        '''
        this function will return the users guess

        Arg:
        self(Dealer): an instance of dealer
        prints card value from deal_card in deck.py

        Attributes:
        asks user to guess hi or low
        '''

        print("The dealers card is: " + str(dealers_card))
        print()
        print(dealers_card)
        print()
        guess = input("Will the next card be higher or lower than the dealers card? (h/l) ")

        return guess

    def deal_cards(self):
        '''
        This function will return the value of a new card.

        Arg: self(Dealer): an instance of dealer
        '''
        return self.deck.deal_card()

    def calculate_points(self, guess, dealers_card):
        '''
        compare the current card with users guess and the next card
        if the same card is drawn a new card is drawn and the function runs again.

        Args:
            self (Dealer): an instance of the dealer class
            guess (str): The users guess which we will compare to the dealers card
            dealers_card: Uses the dealers card to print what total points and and value of the card
        '''
        new_card = self.deal_cards()
        flag = True
        while flag:
            if guess.strip().lower() == "h":
                flag = False
                if dealers_card.value < new_card.value:
                    response = "You won 100 points."
                    self.total_points += 100
                elif dealers_card.value > new_card.value:
                    response = "You lost 75 points."
                    self.total_points -= 75
                else:
                    response = "Draw!"
            elif guess.strip().lower() == "l":
                flag = False
                if dealers_card.value > new_card.value:
                    response = "You won 100 points."
                    self.total_points += 100
                elif dealers_card.value < new_card.value:
                    response = "You lost 75 points."

                    self.total_points -= 75
                else:
                    response = "Draw!"
            else:
                guess = input("Will the next card be higher or lower than the current card? (h/l) ")
        print()
        print("The new card is: " + str(new_card))
        print()
        print(response)
        print()
        print("Your total point are: " + str(self.total_points))
        print()

    def another_round(self):
        '''
        makes the program to tell player if they dont have enough points to keep playing 
        if they get at zero.
        while loop asks if player still wants to play if "y" it will return true,  if "n" it will return false

        '''

        flag = True
        if self.total_points <= 0:
            print("You don't have enough points to continue!")
            print("Game Over!")
            return False
        else:
            while flag:

                play_again = input("Keep playing? (y/n): ")

                if play_again.strip().lower() == "y":
                    return True
                elif play_again.strip().lower() == "n":
                    return False

