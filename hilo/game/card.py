
# Create a dictionary of values: "two" '2', "11", "Jack"
# Create tuple of suits
# Create a tuple of ranks
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
        'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12,'King':13,'Ace':14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

class Card:
    """
    A code template that facilitates the creation of cards.

    Attributes:
    suit (string): Creates a suit for a card
    rank (string): Creates a rank for our card
    value (int): Saves the value of our card
    """
    def __init__(self,suit,rank):
        """The class constructor

        Args:
            self (Card): an instance of Card
            suit (string): stores the suit of the card
            rank (string): stores the rank of the card
        """
        self.suit = suits
        self.rank = ranks
        self.value = values[rank]

    def __str__(self):
        """Allows us to print out the card object

        Returns:
            self (Card): An instance of Card
        """
        return str(self.rank) + " of " + str(self.suit)