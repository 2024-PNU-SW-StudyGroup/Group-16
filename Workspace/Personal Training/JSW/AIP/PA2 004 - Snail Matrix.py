n = int(input())
map = [[0 for _ in range(n)] for _ in range(n)]
cur_y, cur_x = 0, 0
dy, dx = 0, 1
for i in range(n*n):
    if cur_x + dx > n-1 or map[cur_y][cur_x+dx] != 0:
        dy, dx = 1, 0
    if cur_y + dy > n-1 or map[cur_y+dy][cur_x] != 0:
        dy, dx = 0, -1
    if cur_x + dx < 0 or map[cur_y][cur_x+dx] != 0:
        dy, dx = -1, 0
    if cur_y + dy < 0 or map[cur_y + dy][cur_x] != 0:
        dx, dy = 1, 0
        
    map[cur_y][cur_x] = i+1
    cur_x += dx
    cur_y += dy
for y in range(n):
    for x in range(n):
        print(map[y][x], end=" ")
    print()