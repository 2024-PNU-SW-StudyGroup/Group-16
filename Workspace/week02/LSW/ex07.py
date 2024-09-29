#7 369 게임 만들기 : 숫자 3,6,9가 들어가는 경우, 3의배수는 아님
n = int(input("양의 정수를 입력하시오 : "))

def samyukgoo(n):
    temp = n
    digits = []
    digit = temp%10
    while digit != 0 :
        digits.append(digit)
        temp //= 10
        digit = temp%10
    if any(i in digits for i in [3,6,9]):
        print(n, "O")
    else :
        print(n, "X")

for i in range(n):
    samyukgoo(i)