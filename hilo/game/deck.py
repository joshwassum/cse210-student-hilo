import random
import game.card


class Deck:
    """Generate a deck of 52 cards

    Attributes:
    all_cards (list): Stores an instance of each card in our deck.
    """
    def __init__(self):
        """The class constructor.

        Args:
            self (Deck): an instance of Deck
        """
        self.all_cards = []

        for suit in game.card.suits:
            for rank in game.card.ranks:
                created_card = game.card.Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        '''
        This function shuffles our deck

        Args:
            self(Deck): an instance of Deck
        '''
        random.shuffle(self.all_cards)


    def deal_card(self):
        """Prints and then returns the cards value

        Args:
            self(Deck): an instance of Deck
        """

        current_card = self.all_cards.pop()

        return current_card
