class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return "{} of {}".format(self.value, self.suit)


print(13//2)
suits = list(input())
jump = int(input())
deck = []
for i in range(4):
    previous_card = 1
    for j in range(13):
        if previous_card == 13 // jump:
            previous_card = 1
        if previous_card == 1:
            deck.append(Card(suits[i], previous_card))
        else:
            next_card = previous_card + jump
            deck.append(Card(suits[i], next_card))
            previous_card += jump
for card in deck:
    print(card)
