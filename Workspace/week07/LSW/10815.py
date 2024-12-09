sg_n = int(input())
sg_list = [int(i) for i in input().split()]
guess_n = int(input())
guess_list = [int(i) for i in input().split()]

for i in range(len(guess_list)):
    if guess_list[i] in sg_list:
        print(1, end=" ")
    else:
        print(0, end=" ")