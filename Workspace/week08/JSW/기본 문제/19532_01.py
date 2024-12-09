# Problem: 수학은 비대면강의입니다(https://www.acmicpc.net/problem/19532)
# Big O: 
# Comment: Ax = B, x=inv(A)B 사용. 실행시간 20배 단축

def multiplication(v1, v2):
    if len(v1[0]) != len(v2):
        raise Exception("wow")
    result = [[0 for _ in range(len(v2[0]))] for _ in range(len(v1))]
    for i in range(len(v1)):
        for j in range(len(v2[0])):
            result[i][j] = sum([v1[i][k] * v2[k][j] for k in range(len(v1[0]))])
    return result
def inverse(v):
    scalar = v[0][0] * v[1][1] - v[0][1] * v[1][0]
    return [[v[1][1] / scalar, -v[0][1] / scalar], [-v[1][0] / scalar, v[0][0] / scalar]]

a, b, c, d, e, f = map(int, input().split())
v1 = [[a, b],
      [d, e]]

v2 = [[c],
      [f]]

x, y = multiplication(inverse(v1), v2)
result = f"{int(round(x[0]))} {int(round(y[0]))}"
print(result)