from collections import Counter
# Hands:
# Straight flush
# Four of a kind
# Full house
# Flush
# Straight
# Three of a kind
# Two pair
# Pair
# High card

cards = list(range(14))
suitDict = {"Hearts": 0, "Diamonds":1, "Clubs":2, "Spades":3}
suits=list(range(4))

def pair(cards,suits):
    return len([x for x in Counter(cards) if Counter(cards)[x]==2])==1

def twoPair(cards,suits):
    return len([x for x in Counter(cards) if Counter(cards)[x]==2])==2

def threeOfAKind(cards,suits):
    return len([x for x in Counter(cards) if Counter(cards)[x]==3])==1

def fullHouse(cards,suits):
    return pair(cards,suits) and threeOfAKind(cards, suits)

def fourOfAKind(cards,suits):
    return len([x for x in Counter(cards) if Counter(cards)[x]==4])==1

def flush(cards,suits):
    return len([x for x in Counter(suits) if Counter(suits)[x]==5])==1

def straight(cards,suits):
    srtd=sorted(cards)
    if(srtd==list(range(min(cards), max(cards)+1))): return True
    return srtd[0]==1 and srtd[1:]==list(range(min(srtd[1:]), max(srtd[1:])+1))

def flushStraight(cards,suits):
    return flush(cards,suits) and straight(cards,suits)

