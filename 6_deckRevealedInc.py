def deckRevealedIncreasing(deck):
    deck.sort()
    result = []
    
    for card in reversed(deck):
        if result:
            result.insert(0, result.pop())
        result.insert(0, card)
    
    return result




print(deckRevealedIncreasing([17,13,11,2,3,5,7]))  # Output: [2, 13, 3, 11, 5, 17, 7]
print(deckRevealedIncreasing([1, 1000]))          # Output: [1, 1000]
