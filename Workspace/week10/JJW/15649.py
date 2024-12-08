'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
'''

# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

# 이해할 때 참고한 사이트: https://goldenrabbit.co.kr/2023/12/29/%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%95%A9%EA%B2%A9%EC%9E%90-%EB%90%98%EA%B8%B0-%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9-1-%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9%EA%B3%BC-%EB%B0%B1/
'''
M = 3
N = 3
result_list = []

def list_checker(num, list):
    for i in range(len(list)):
        if num == list[i]:
            return False
        else:
            return True


def recurse(depth, list):
    if depth == M:
        print(list)
    else:
        for i in range(len(list)):
            if list_checker(i, list):
                list.append(i)
                return recurse(depth + 1, list)    


for i in range(1, N + 1):
    result_list.append(i)
    recurse(1, result_list)
    result_list.clear
'''

def duplication_check(num, list):
    i = 0
    for i in range(list):
        if num == list[i]:
            return False
    return True

def number_sequence(N, M):
    i = 0
    list = []
    depth = len(list)
    if depth == N:
        return list
    else:
        while i < len(list):
            