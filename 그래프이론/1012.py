T = int(input())
movement = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # up, down, right, left


def bfs(N, M, MAP, visited, x, y):
    queue = []
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        position = queue.pop(0)
        for i in range(4):
            coordinate = (position[0] + movement[i][0], position[1] + movement[i][1])
            if coordinate[0] < 0 or coordinate[0] >= N:
                continue
            if coordinate[1] < 0 or coordinate[1] >= M:
                continue
            if MAP[coordinate[0]][coordinate[1]] == 0:
                continue
            if visited[coordinate[0]][coordinate[1]] == 1:
                continue
            if MAP[coordinate[0]][coordinate[1]] == 1:
                visited[coordinate[0]][coordinate[1]] = 1
                queue.append((coordinate[0], coordinate[1]))


def set():
    M, N, K = map(int, input().split())
    MAP = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    count = 0
    for i in range(K):
        a, b = map(int, input().split())
        MAP[b][a] = 1

    for i in range(N):
        for j in range(M):
            if visited[i][j] == 1:
                continue
            if MAP[i][j] == 1:
                bfs(N, M, MAP, visited, i, j)
                count += 1
    return count

def solve():
    answer = []
    for i in range(T):
        x = set()
        answer.append(x)

    for i in range(T):
        print(answer[i])

solve()