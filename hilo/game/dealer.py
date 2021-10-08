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

        while self.keep_playing:
            dealers_card = self.deal_cards()
            user_guess = self.guess_hi_low(dealers_card)
            self.deal_cards()
            self.score()

    def guess_hi_low(self, dealers_card):
        '''
        this function will return the users guess

        Arg:
        prints card value from deal_card in deck.py

        Attributes:
        asks user to guess hi or low
        '''
        print(self.current_card)
        print()
        guess = input("Will the next card be higher or lower than the current card? (h/l) ")

        return guess

    def deal_cards(self):
        '''
        This function will return the value of a new card.
        '''
        return self.deck.deal_card()

    def calculate_points(self, guess):
        '''
        compare the current card with users guess and the next card
        if the same card is drawn a new card is drawn and the function runs again.

        Args:
            self (Dealer): an instance of the dealer class
            guess (str): The users guess which we will compare to the dealers card
        '''
        print()
        if self.guess_hi_low().strip().lower() == "h":
            if self.current_card < self.deal_cards():
                print("you won 100 points.")
                self.total_points += 100
            elif self.current_card > self.deal_cards():
                print("you lost 75 points")
                self.total_points -= 75
            elif self.current_card == self.deal_cards():
                self.calculate_points()
        if self.guess_hi_low().strip().lower == "l":
            if self.current_card > self.deal_cards():
                print("you won 100 points.")
                self.total_points += 100
            elif self.current_card < self.deal_cards():
                print("you lost 75 points")
                self.total_points -= 75
            elif self.current_card == self.deal_cards():
                self.calculate_points()
        print()
        print(self.total_points)

