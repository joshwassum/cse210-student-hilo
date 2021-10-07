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
    starts game (larry)

    ask to play again (shane)
        end game if points is 0

    deal cards (Brian)
        ask hi or low
    
    calculate points (brian)
        compare values and award points
    '''