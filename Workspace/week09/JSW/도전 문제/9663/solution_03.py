# Problem: N-Queen(https://www.acmicpc.net/problem/9663)
# Date: 2024.11.25
# Comment: solution_01 코드에서 굳이 answer들을 history에 저장할 필요가 없으므로 갯수만 세자.
# -> 시간 초과.
# -> 파이썬이 문제인가? 무적의 C++로 풀어보자.
# -> 파이썬이 문제였음. 
# -> 다른 사람들이 푼 코드들을 보면 n=13부터는 양심없게 저장된 답을 출력시킴.

def solution(N):
    answer = [0]*N
    visited = [False]*N
    history = 0
    def is_valid(state, depth):
        y_0 = y_1 = state[depth-1]
        for i in range(depth-2, -1, -1):
            y_0, y_1 = y_0-1, y_1+1
            if y_0 == state[i] or y_1 == state[i]: return False
        return True
    def recurse(depth):
        if not is_valid(answer, depth):
            return
        if depth == N:
            nonlocal history
            history += 1
            return
        for i in range(N):
            if visited[i]: continue
            answer[depth] = i
            visited[i] = True
            recurse(depth+1)
            visited[i] = False
    recurse(0)
    return history

N = int(input())
print(solution(N))
