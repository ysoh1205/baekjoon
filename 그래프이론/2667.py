N = int(input())
MAP = [list(map(int, input().rstrip())) for _ in range(N)]

stack = []
visited = [[0]*N for _ in range(N)]

movement = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # up, down, right, left


def bfs(x, y):
    queue = []
    count = 0
    queue.append((x,y))
    visited[x][y] = 1
    while queue:
        position = queue.pop(0)
        count += 1
        for i in range(4):
            coordinate = (position[0] + movement[i][0], position[1] + movement[i][1])
            if coordinate[0] < 0 or coordinate[0] >= N:
                continue
            if coordinate[1] < 0 or coordinate[1] >= N:
                continue
            if MAP[coordinate[0]][coordinate[1]] == 0:
                continue
            if visited[coordinate[0]][coordinate[1]] == 1:
                continue
            if MAP[coordinate[0]][coordinate[1]] == 1:
                visited[coordinate[0]][coordinate[1]] = 1
                queue.append((coordinate[0], coordinate[1]))
    stack.append(count)

def solve():

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                continue
            if MAP[i][j] == 1:
                bfs(i, j)

solve()
stack.sort()
print(len(stack))
for i in range(len(stack)):
    print(stack[i])