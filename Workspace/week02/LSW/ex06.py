#6 숫자 뒤집기
userInput = int(input("양의 정수를 입력하시오 : "))

"""
사기꾼 방식

tempstr = list(str(userInput))
result = []
for i in range(len(tempstr)):
    result.append(tempstr.pop())
print("".join(result))
"""
digits =[]
digit = userInput%10
temp = userInput
result = 0
while digit != 0 :
    digits.append(digit)
    temp //= 10
    digit = temp%10
for i in range(len(digits)):
    result+=digits[i]*10**(len(digits)-i-1)
print(result)