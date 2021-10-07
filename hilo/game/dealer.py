import deck


class Dealer:

    '''
    Attributes:
    call the deck class
    continue playing?
    total points
    '''

    def __init__(self):

        self.deck = deck.Deck()
        self.coninue_play = True
        self.total_points = 300

    '''
    Methods:
    starts game
    ask to play again
        end game if points is 0
    deal cards (Brian)
    calculate points
        compare values and award points
    '''