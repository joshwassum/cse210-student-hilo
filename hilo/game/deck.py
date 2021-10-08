import random
from game.card import Card

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

        for suit in Card.suits:
            for rank in Card.ranks:
                created_card = Card.Card(suit,rank)
                self.all_cards.append(created_card)


    def deal_card(self):
        """Prints and then returns the cards value

        Args:
            self(Deck): an instance of Deck
        """
        current_card = self.all_cards[random.randint(1, 14)]
        return current_card.value