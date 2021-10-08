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
        self.continue_play = True
        self.total_points = 300

    
    def start_game(self):
        '''
        starts game loop 

        Arg: self(Dealer): an instance of dealer
        '''

        while self.keep_playing:
            self.deck()
            self.deal_cards()
            self.score()
        



    '''
    ask to play again (shane)
        end game if points is 0

    deal cards (Brian)
        hi or low
    
    calculate points (brian)
        compare values and award points
    '''