#5 3과 5의 배수 계산하기
n = int(input())
lists = []
def calc3and5(user_input):
    if (user_input%5==0 and user_input%3==0) :
        print(user_input,"은 3의 배수이면서 5의 배수입니다.")
        lists.append(user_input)
    else:
        print(user_input, "은 3의 배수이면서 5의 배수가 아닙니다.")
for i in range(n):
    calc3and5(i+1)

for i in lists:
    print(i)