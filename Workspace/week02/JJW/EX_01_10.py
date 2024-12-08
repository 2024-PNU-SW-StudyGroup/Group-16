# EX_01
'''반복문을 사용하여 0부터 n까지의 합 출력하기
조건:
1. 1이 아니라 0부터 100까지의 숫자를 순서대로 증가시켜야 한다.
2. 숫자를 순서대로 증가시키는 방법으로 반복문을 사용해야 한다.
3. 이 프로그램에서 사용하는 변수의 개수를 미리 알고 있어야 한다.'''

'''끄적끄적:
'''

# 직접 만든 버전
total = 0
var = 0
while (var <= 100):
    total = total + var
    var = var + 1

print(total)

# 책보고 만든 버전
def print_to_n(n):
    i = 0
    sum = 0
    while (i <= n):
        sum = sum + i
        i = i + 1
    print(sum)

print_to_n(100)

#if__name__=="__main__":
#    print_to_n(100)

# EX_02
'''재귀 호출을 사용하여 1부터 20까지 출력하기
조건:
1. 1부터 출력해야 한다.
2. 재귀 호출을 빠져 나오는 제어 조건을 명확하게 정의해야 한다.
3. 재귀 함수의 호출과 재귀 함수 내의 처리 문장의 실행 순서를 명확하게 정의해야 한다.'''

'''끄적끄적:
'''

# 직접 만든 버전
num = 1
max_num = 20
def rec(n):
    if n == max_num + 1:
        exit
    else:
        print(n)
        rec(n + 1)
rec(num)


# 책 보고 만든 버전, 분명 1부터 출력하라 했는데 왜 0부터지
def print_to_n(n):
    if n > 0:
        print_to_n(n - 1)
    print(n)

print_to_n(20) #확인용

if'___name___'=="___main___": # 이거 사용방법을 잘모르겠다.
    print_to_n

# EX_03
'''반복문을 사용하여 1부터 n까지 출력하기
조건:
1. 1부터 순서대로 화면에 출력해야 한다.
2. 출력하는 숫자가 n이 되면 프로그램을 종료한다.'''

'''끄적끄적:
'''

# 직접 만든 버전
n = 1
while (n <= 20):
    print(n)
    n += 1


# 책보고 만든 버전
n = 20
c = 1
while (c <= n):
    print(c)
    c = c + 1

# EX_04
'''재귀 호출을 사용하여 n부터 1까지 출력하기
조건
1. n부터 1까지 역순으로 화면에 출력해야 한다.
2. 출력하는 숫자가 1이되면 프로그램을 종료한다.'''

'''끄적끄적:
'''

# 직접 만든 버전
def print_rev(n):
    if n > 0:
        print(n)
        print_rev(n - 1)
    else: exit

print_rev(10)


# 책보고 만든 버전
def print_to_n(n):
    print(n, end = ' ')
    if n > 1:
        print_to_n(n - 1)

print_to_n(10)

'''if___name___=="___main___":
    print_to_n(10)'''

# EX_05
'''조건:
1. 배수의 개념을 코드로 만들 수 있어야 한다.
2. 3의 배수이면서 동시에 5의 배수인지를 확인하는 개념을 코드로 만들 수 있어야 한다.
3. 반복문을 사용하여 1부터 n까지 1씩 증가하면서 제어 변수를 확인한다.'''

'''끄적끄적:
3, 5 나누기
둘다 나눠지면 배수 확인
'''
# 직접 만든 버전
n = 1
def inspector(n):
    if n % 3 == 0 and n % 5 == 0:
        print("3과 5의 배수", end = " \n")
    elif n % 3 == 0:
        print("3의 배수는 맞아요", end = " \n")
    elif n % 5 == 0:
        print("5의 배수는 맞아요", end = " \n")

while (n <= 30):
    print(n)
    inspector(n)
    n += 1


# 책보고 만든 버전
def check_common(n):
    i = 1
    while i <= n:
        if (i % 3 == 0) and (i % 5 == 0):
            print("%d"%i)
        i = i + 1

check_common(100)

'''if___name___=="___main___":
    check_common(100)'''

# EX_06
'''숫자 뒤집기
조건:
1. 정수의 자릿수를 계산 하는 방식을 고민해야 한다.
2. 이 문제의 경우는 반복문보다는 재귀 호출을 응용하는 것이 간단하다.'''

'''끄적끄적:
십진수니까 10으로 나누기
순서 다시 정렬할때 10 곱하기'''

# 직접 만든 버전
def num_reverse_machine(n):
    print(n % 10, end = "")
    if (n < 10): exit
    else:
        num_reverse_machine(n // 10)
num_reverse_machine(123456789)

# 책보고 만든 버전
def solve(n):
    if n == 0:
        return 0
    print(n % 10, end = '')
    solve(n // 10)

num_str = input("입력: ")
num = int(num_str)
solve(num)

'''if___name___=="___main___":
    num_str = input("입력: ")
    num = int (num_str)
    solve(num)'''

# EX_07
'''369 게임 만들기
조건:
1. 3의 배수를 확인하는 코드를 작성해야 한다.
2. 3의 배수가 아닌 경우는 숫자를 출력하고, 3의 배수인 경우는 "X"를 출력하는 코드를 작성해야 한다.
3. 사용자로부터 입력 받은 n까지 위의 과정을 반복해야 한다.'''

'''끄적끄적:
3으로 나눈 나머지로 판별
나눠서 print로 X 출력
input으로 n 입력받기'''

# 직접 만든 버전
def JDG_369(n):
    print(n, end = ' ')
    if n % 3 == 0:
        print("X")
    else:
        print("통과!")

num_str = input("값을 주세요: ")
num = int(num_str)
cnt = 1

while (num > 0):
    JDG_369(cnt)
    cnt += 1
    num -= 1

# 책보고 만든 버전
def solve(n):
    i = 1
    while i <= n:
        if i % 3 == 0:
            print("X")
        else:
            print(i)
        i = i + 1
solve(30)
'''if___name___=="__main__":
    solve(30)'''

# EX_08
'''자연수 n이 소수인지 아닌지를 출력하기
조건:
1. 반복문을 사용하여 주어진 숫자 n을 2부터 n - 1까지 반복하면서 나누고, 나눈 결과가 하나라도 나눈 몫을 구할 수 있으면 소수가 아닌 합성수이다.
2. 위의 반복문이 끝난 결과로 제어 변수가 주어진 n과 같으면 소수이고 같지 않으면 합성수이다.'''

'''끄적끄적:
조건에서 시키는 대로 하기'''

# 직접 만든 버전
num_str = input("입력하셈~: ")
num = int(num_str)
detector = 0
for i in range(2, num - 1):
    if num % i == 0:
        detector += 1
if detector > 0:
    print("합성수desu")
else:
    print("소수desu")

# 책보고 만든 버전
def check_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            break
        i = i + 1
    if i == n:
        print("{0}는 소수\n".format(n))
    else:
        print("{0}는 합성수\n".format(n))

check_prime(19)
check_prime(130)
check_prime(37)
check_prime(20)
check_prime(21)

'''if___name___=="__main__":
    check_prime(19)'''

# EX_09
'''2 ~ N 사이의 모든 소수를 추출하기
조건:
1. 2부터 N까지의 반복문으로 소수 확인 함수를 호출한다.'''

'''끄적끄적:
EX_08에서 만든 코드 개조하기'''

# 직접 만든 버전
num_str = input("입력desu: ")
num = int(num_str)
def prime_detector(n):
    for i in range(2, n - 1):
        if n % i == 0:
            print("%d 얘는 평범한 합성수임"%n)
            return 0
    print("%d 얘는 유명한 소수임"%n)

for i in range(2, num + 1):
    prime_detector(i)

# 책보고 만든 버전
def check_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            break
        i = i + 1
    if i == n:
        print("{0}는 소수\n".format(n))
    else:
        print("{0}는 합성수\n".format(n))

i = 2
while i <= 20:
    check_prime(i)
    i = i + 1

'''if___name___=="__main__":
    i = 2
    while i <= 20:
        check_prime(i)
        i = i + 1'''

# EX_10
'''약수 구하기
조건:
1. n의 약수를 구하기 위해서 2부터 n의 제곱근까지만 탐색한다.
2. 소수가 아닌 경우에는 약수를 구해야 하기 때문에 이전의 소수를 구하는 문제와는 달리 break문을 사용할 수 없다.
3. 소수인지 아닌지를 저장해두기 위해 플래그 변수를 사용한다.'''

'''끄적끄적:
소수 찾는 함수에서 그대로 소수아니고 0으로 나누어지는 경우는 약수로 추출하기 <- 생각을 잘못했다.'''

# 직접 만든 버전
num_str = input("입력desu: ")
num = int(num_str)
def aliquat_detector(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print("{0} 얘는 {1}의 약수임".format(i, n))

aliquat_detector(num)

# 책보고 만든 버전
def solve(n):
    ans = 0

    i = 1
    while i <= n:
        if n % i == 0:
            print("약수 : {0}".format(i))
        i = i + 1

n = int(input("입력:"))
solve(n)

'''if___name___=="__main__":
    n = int(input("입력:"))
    solve(n)'''