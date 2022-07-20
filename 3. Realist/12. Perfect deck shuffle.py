def perfect_shuffle(deck: list):
    new_deck: list = []
    half_len = int(len(deck) * 0.5)
    deck1 = deck[: half_len]
    deck2 = deck[half_len:]
    for i in range(half_len):
        new_deck.append(deck1[i])
        new_deck.append(deck2[i])
    return new_deck


if __name__ == "__main__":
    print(perfect_shuffle([1, 2, 3, 4, 5, 6]))