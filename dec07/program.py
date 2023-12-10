import sys
from collections import Counter
from itertools import product
CARDS = 'AKQT98765432J'
    
class Hand:

    def __init__(self, hand: str):
        self.hand = hand
        self.score = self.find_score(hand)

    def findOccurrences(self, string: str, ch: str) -> list[int]:
        return [i for i, letter in enumerate(string) if letter == ch]

    def find_score(self, hand: str) -> int:
        # Check for five of a kind
        jokers = self.findOccurrences(hand, 'J')
        max_score = -1
        tests = product(CARDS, repeat=len(jokers))
        for test in tests:
            # Create new "hand"
            new_hand = list(hand)
            for idx, j in enumerate(jokers):
                new_hand[j] = test[idx]
            counts = Counter(new_hand)
            if len(counts) == 1:
                return 6
            # Check for four of a kind
            elif (len(counts) == 2) and (4 in counts.values()):
                # return 5
                max_score = max(max_score, 5)
            # Check for full house
            elif (len(counts) == 2) and (3 in counts.values()):
                # return 4
                max_score = max(max_score, 4)
            # Check for three of a kind
            elif (len(counts) == 3) and (3 in counts.values()):
                # return 3
                max_score = max(max_score, 3)
            # Check for two pair
            elif (len(counts) == 3):
                # return 2
                max_score = max(max_score, 2)
            elif (len(counts) == 4) and (2 in counts.values()):
                # return 1
                max_score = max(max_score, 1)
            else:
                # return 0
                max_score = max(max_score, 0)
        return max_score

    
    def __eq__(self, other):
        return self.hand == other.hand

    def __lt__(self, other):
        if self.score != other.score:
            return self.score < other.score
        if self.hand == other.hand:
            return False
        for card1, card2 in zip(self.hand, other.hand):
            if card1 != card2:
                return CARDS.find(card1) > CARDS.find(card2)
        return False
    
    def __gt__(self, other):
        if self.score != other.score:
            print('returning early')
            return self.score > other.score
        if self.hand == other.hand:
            print('returning false here')
            return False
        for card1, card2 in zip(self.hand, other.hand):
            print(f'checking card1 {card1} and card2 {card2}')
            if card1 != card2:
                return CARDS.find(card1) < CARDS.find(card2)
        return False
    
    def __repr__(self):
        return self.hand
    def __str__(self):
        return self.hand



def puzzle1():
    hands = list()
    hands_to_bids = dict()
    for line in sys.stdin.readlines():
        hand = Hand(line.split(' ')[0].rstrip())
        hands.append(hand)
        hands_to_bids[hand.hand] = int(line.split(' ')[1].rstrip())
    hands.sort(reverse=True)
    total_winnings = 0
    for idx, hand in enumerate(hands):
        total_winnings += ((len(hands)-idx) * hands_to_bids[hand.hand])
    print(f'The answer to puzzle 1 is {total_winnings}')



def puzzle2():
    hands = list()
    hands_to_bids = dict()
    for line in sys.stdin.readlines():
        hand = Hand(line.split(' ')[0].rstrip())
        hands.append(hand)
        hands_to_bids[hand.hand] = int(line.split(' ')[1].rstrip())
    hands.sort(reverse=True)
    total_winnings = 0
    for idx, hand in enumerate(hands):
        total_winnings += ((len(hands)-idx) * hands_to_bids[hand.hand])
    print(f'The answer to puzzle 2 is {total_winnings}')



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        puzzle1()
    elif sys.argv[1] == '2':
        puzzle2()