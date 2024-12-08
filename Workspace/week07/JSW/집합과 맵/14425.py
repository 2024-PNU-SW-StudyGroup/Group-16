# 문자열 집합
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
word_set = set([input() for _ in range(N)])

print(sum([1 for _ in filter(lambda x: x in word_set, [input() for _ in range(M)])]))