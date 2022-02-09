N, M = map(int, input().split())
MAP = [list(map(int, input().rstrip())) for _ in range(N)]

queue = []  # (depth, (${coordinate}), move)
queue.append((0, 0))

movement = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # up, down, right, left


def solve():
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
            if MAP[coordinate[0]][coordinate[1]] == 1:
                MAP[coordinate[0]][coordinate[1]] = MAP[position[0]][position[1]] + 1
                queue.append((coordinate[0], coordinate[1]))

    print(MAP[N-1][M-1])

solve()