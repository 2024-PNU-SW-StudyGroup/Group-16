# Problem: 블랙잭(https://www.acmicpc.net/problem/2798)
# Algorithm: 
# Big-O: NlogN

N, M = map(int, input().split())
cards = list(map(int, input().split()))

cards.sort(reverse=True)
print(cards)
slider = sum(cards[:3])
for i in range(3, N):
    slider += cards[i]
    if slider <= M:
        print(slider)
        exit()
    slider -= cards[i-3]