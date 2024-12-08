my_string = input()
result = []
for i in range(len(my_string)):
    if my_string[i].isdigit():
        result.append(int(my_string[i]))
print(sum(result))