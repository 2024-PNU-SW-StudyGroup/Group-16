# Problem: N과 M (3) (https://www.acmicpc.net/problem/15651)
# Date: 2024.11.18
# Comment
# - 15651_01.py는 실행 시간이 너무 컸음.. -> history 삭제, stdout 사용

import sys
def product(iterable, repeat):
    def recurse(iterable, r, temp):
        if r == 0:
            sys.stdout.write(" ".join(temp))
            sys.stdout.write('\n')

            return
        for e in iterable:
            temp.append(e)
            recurse(iterable, r-1, temp)
            temp.pop()
    recurse(iterable, repeat, [])

N, M = map(int, input().split())
product([chr(ord('1') + i) for i in range(N)], repeat=M)
sys.stdout.close()