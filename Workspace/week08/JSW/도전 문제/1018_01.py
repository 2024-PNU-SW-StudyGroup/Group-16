# Problem: 체스판 다시 칠하기(https://www.acmicpc.net/problem/1018)
# Comment: 
# - 효율적인 cache 사용을 위해, 2차원 list 대신에 1차원 list로 변경 -> 크게 영향 없어서 롤백
# - 0인 diff를 발견하면 조기 종료
# - mask를 1개로 줄임
import sys
input = sys.stdin.readline
mask = [[(i+j)%2 for j in range(8)] for i in range(8)]
def cal_diff(board, r, c):
    diff_01, diff_02 = 0, 0
    for i in range(8):
        for j in range(8):
            temp = mask[i][j] ^ board[r+i][c+j]
            diff_01 += temp
            diff_02 += not temp
    return min(diff_01, diff_02)

encoding = lambda x: 0 if x == 'W' else 1 
M, N = map(int, input().split())
board = [list(map(encoding, input())) for _ in range(M)]
min_diff = 8*8
for r in range(M-7):
    for c in range(N-7):
        min_diff = min(min_diff, cal_diff(board, r, c))
        if min_diff == 0:
            break
print(min_diff)