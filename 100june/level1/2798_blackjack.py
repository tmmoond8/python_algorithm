import sys

N, B = map(int, sys.stdin.readline().strip().split(' '))
cards = list(map(int, sys.stdin.readline().strip().split(' ')))

def allSum(cards, black_jack):
    S = set()
    L = len(cards)
    for i in range(0, L - 2):
        for j in range(i + 1, L - 1):
            for k in range(j + 1, L):
                if cards[i] + cards[j] + cards[k] <= black_jack:
                    S.add(cards[i] + cards[j] + cards[k])
    ol = list(S)
    ol.sort()
    print(ol.pop())


allSum(cards, B)