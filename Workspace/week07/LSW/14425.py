n, m = map(int, input().split())
s_set = {input().strip() for _ in range(n)}
count = 0

for _ in range(m):
    if input().strip() in s_set:
        count += 1

print(count)