# Problem: 체스판 다시 칠하기(https://www.acmicpc.net/problem/1018)
# Comment:
# 

sol_01 = [[(i+j)%2 for j in range(8)] for i in range(8)]
sol_02 = [[(i+j+1)%2 for j in range(8)] for i in range(8)]
def cal_diff(board, r, c):
    diff_01, diff_02 = 0, 0
    for i in range(8):
        for j in range(8):
            if board[r+i][c+j] != sol_01[i][j]:
                diff_01 += 1
            if board[r+i][c+j] != sol_02[i][j]:
                diff_02 += 1
    return min(diff_01, diff_02)

encoding = lambda x: 0 if x == 'W' else 1 
M, N = map(int, input().split())
board = [list(map(encoding, input())) for _ in range(M)]
min_diff = 8*8
for r in range(M-7):
    for c in range(N-7):
        min_diff = min(min_diff, cal_diff(board, r, c))
print(min_diff)