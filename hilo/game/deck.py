import random
import card

class Deck:
    """Generate a deck of 52 cards and then shuffle them

    Attributes:
    all_cards = list
    """
    def __init__(self):

        self.all_cards = []

        for suit in card.suits:
            for rank in card.ranks:
                created_card = card.Card(suit,rank)
                self.all_cards.append(created_card)

    """Ability to deal a random card

    Brian Bawden
    """
