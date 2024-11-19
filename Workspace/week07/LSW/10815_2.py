sg_n = int(input())
sg_list = set(map(int, input().split()))
guess_n = int(input())
guess_list = list(map(int, input().split()))

print(' '.join('1' if num in sg_list else '0' for num in guess_list))