#opensource code from https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards


class Card(object):

    card_values = {
        'Ace': 11,  # value of the ace is high until it needs to be low
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10,
        'ACE' : 1
        
        
    }

    def __init__(self, suit, rank):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param rank: The value of the card, e.g 3 or King
        """
        self.suit = suit.capitalize()
        self.rank = rank
        self.points = self.card_values[rank]

CARD = """\
┌─────────┐
│{}       │
│         │
│         │
│    {}   │
│         │
│         │
│       {}│
└─────────┘
""".format('{rank: <2}', '{suit: <2}', '{rank: >2}')

HIDDEN_CARD = """\
┌─────────┐
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
└─────────┘
"""

def join_lines(strings):
    """
    Stack strings horizontally.
    This doesn't keep lines aligned unless the preceding lines have the same length.
    :param strings: Strings to stack
    :return: String consisting of the horizontally stacked input
    """
    liness = [string.splitlines() for string in strings]
    return '\n'.join(''.join(lines) for lines in zip(*liness))

def ascii_version_of_card(*cards):
    """
    Instead of a boring text version of the card we render an ASCII image of the card.
    :param cards: One or more card objects
    :return: A string, the nice ascii version of cards
    """
    test = []
    for b in range(len(cards[0])):
        test.append(cards[0][b])

    # we will use this to prints the appropriate icons for each card
    name_to_symbol = {
        'Spades':   '♠',
        'Diamonds': '♦',
        'Hearts':   '♥',
        'Clubs':    '♣',
    }

    def card_to_string(card):
        # 10 is the only card with a 2-char rank abbreviation
        rank = card.rank if card.rank == '10' else card.rank[0]

        # add the individual card on a line by line basis
        return CARD.format(rank=rank, suit=name_to_symbol[card.suit])


    return join_lines(map(card_to_string, test))


def ascii_version_of_hidden_card(*cards):
    """
    Essentially the dealers method of print ascii cards. This method hides the first card, shows it flipped over
    :param cards: A list of card objects, the first will be hidden
    :return: A string, the nice ascii version of cards
    """
    test = []
    for b in range(len(cards[0])):
        test.append(cards[0][b])

    return join_lines((HIDDEN_CARD, ascii_version_of_card(test[:1])))


## TEST CASES
#test_card_1 = Card('Diamonds', '4')
#test_card_2 = Card('Clubs', 'Ace')
#test_card_3 = Card('Spades', 'Jack')
#test_card_4 = Card('Hearts', '10')

#print(ascii_version_of_card(test_card_1, test_card_2, test_card_3, test_card_4))
#print(ascii_version_of_hidden_card(test_card_1, test_card_2, test_card_3, test_card_4))
##print(ascii_version_of_hidden_card(test_card_1, test_card_2))