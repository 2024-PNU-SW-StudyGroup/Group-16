#4 재귀 호출을 사용하여 n부터 1까지 출력하기
def reverseCalc(n):
    if n>=1:
        print(n)
        n-=1
        return reverseCalc(n)
    else : return 0

reverseCalc(int(input('n을 입력하시오 : ')))
