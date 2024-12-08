# Problem: N-Queen(https://www.acmicpc.net/problem/9663)
# Date: 2024.11.25
# Comment: 
# 적절하게 state space를 구성하고 백트래킹을 사용하여 코드를 작성하였다.
# -> 시간초과
# -> 일단 코드가 맞는지 확인하기 위해 N이 [1,15)일 때의 결과값을 배열에 저장하여 제출해보자.

def solution(N):
    answer = [0]*N
    visited = [False]*N
    history = []
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
            history.append(answer[:])
            return
        for i in range(N):
            if visited[i]: continue
            answer[depth] = i
            visited[i] = True
            recurse(depth+1)
            visited[i] = False
    recurse(0)
    return len(history)

N = int(input())
print(solution(N))
