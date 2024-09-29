#재귀 호출을 사용하여 1부터 20까지 출력하기
def calc(n) :
    if n<20:
        print(n)
        n+=1
        return calc(n)
    else :
        return 0