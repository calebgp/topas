def calcPoints(deck):
    points = 0
    counted_cards = set()
    for card in deck:
        if deck.count(card) >= 4 and card not in counted_cards:
            points += 10 * card
            counted_cards.add(card)
        elif deck.count(card) == 3 and card not in counted_cards:
            points += 5 * card
            counted_cards.add(card)
        elif deck.count(card) == 2 and card not in counted_cards:
            points += 3 * card
            counted_cards.add(card)
        elif card not in counted_cards:
            points += card
    return points


def winners(players):
    max_points = 0
    winners = 0
    for deck in players:
        points = calcPoints(deck)
        if points > max_points:
            max_points = points
            winners += 1
        elif points == max_points:
            winners += 1
    return winners, max_points


nPlayers = int(input())
decks = []
for _ in range(nPlayers):
    deck = list(map(int, input().split()))
    decks.append(deck)
winners, points = winners(decks)

print(f'{winners} {points}')
