n = int(input())
enter_set = set()
for i in range(n):
    name, status = input().split()
    if status == "enter":
        enter_set.add(name)
    elif status == "leave":
        enter_set.discard(name)
sorted_set = sorted(enter_set, reverse=True)

for i in sorted_set:
    print(i)