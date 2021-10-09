# Tasking
'''
ask to play again (shane)
    end game if points is 0

deal cards (Brian)
    hi or low

calculate points (brian)
    compare values and award points
'''


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

        Arg: self(Dealer): an instance of dealer
        """

        self.deck = Deck()
        self.keep_playing = True
        self.total_points = 300

    def start_game(self):
        '''
        starts game loop

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
        prints card value from deal_card in deck.py

        Attributes:
        asks user to guess hi or low
        '''
        print(dealers_card)
        print()
        guess = input("Will the next card be higher or lower than the current card? (h/l) ")

        return guess

    def deal_cards(self):
        '''
        This function will return the value of a new card.
        '''
        return self.deck.deal_card()

    def calculate_points(self, guess, dealers_card):
        '''
        compare the current card with users guess and the next card
        if the same card is drawn a new card is drawn and the function runs again.

        Args:
            self (Dealer): an instance of the dealer class
            guess (str): The users guess which we will compare to the dealers card
        '''
        new_card = self.deal_cards()
        flag = True
        while flag:
            if guess.strip().lower() == "h":
                flag = False
                if dealers_card.value < new_card.value:
                    print("you won 100 points.")
                    self.total_points += 100
                elif dealers_card.value > new_card.value:
                    print("you lost 75 points")
                    self.total_points -= 75
                else:
                    print("Draw!")
            elif guess.strip().lower() == "l":
                flag = False
                if dealers_card.value > new_card.value:
                    print("you won 100 points.")
                    self.total_points += 100
                elif dealers_card.value < new_card.value:
                    print("you lost 75 points")
                    self.total_points -= 75
                else:
                    print("Draw!")
            else:
                guess = input("Will the next card be higher or lower than the current card? (h/l) ")
        print()
        print(new_card)
        print()
        print(self.total_points)
        print()

    def another_round(self):
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

