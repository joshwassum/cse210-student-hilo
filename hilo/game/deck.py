import random
import card

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

        for suit in card.suits:
            for rank in card.ranks:
                created_card = card.Card(suit,rank)
                self.all_cards.append(created_card)


    def deal_card(self):
        """Prints and then returns the cards value

        Args:
            self(Deck): an instance of Deck
        """
        current_card = self.all_cards[random.randint(1, 14)]
        return current_card.value