N, M = map(int, input().split())
MAP = [list(input().rstrip()) for _ in range(N)]
movement = [(0,1), (0,-1), (1,0), (-1,0)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
queue = []

rx, ry, bx, by = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 'R':
            rx, ry = i, j
        elif MAP[i][j] == 'B':
            bx, by = i, j

visited[rx][ry][bx][by] = True
queue.append((rx, ry, bx, by, 1))

def move(x, y, dx, dy):
    while MAP[x+dx][y+dy] != '#' and MAP[x+dx][y+dy] != 'O':
        x += dx
        y += dy
    return x, y

while queue:
    rx, ry, bx, by, depth = queue.pop(0)
