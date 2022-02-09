import copy

N = int(input())
MAP = [list(map(int, input().rstrip().split())) for _ in range(N)]
queue = []
maxSet = [0]
movement = [(0,1), (0,-1), (1,0), (-1,0)]


def init(MAP):
    cp = copy.deepcopy(MAP)
    queue.append((tuple(map(tuple, cp)), 0, -1)) #(map, depth, move)


init(MAP)


def count0(MAP, x, y, dx, dy):
    cnt = 0
    if dx == 0 and dy == 1:
        while MAP[x][y] == 0:
            cnt += 1
            x += 1
    elif dx == 0 and dy == -1:
        while MAP[x][y] == 0:
            cnt += 1
            x -= 1
    elif dx == 1 and dy == 0:
        while MAP[x][y] == 0:
            cnt += 1
            y -= 1
    elif dx == -1 and dy == 0:
        while MAP[x][y] == 0:
            cnt += 1
            y += 1
    return cnt


def move(MAP, dx, dy, depth):
    isMoved = False
    cp = copy.deepcopy(MAP)
    if dx == 0 and dy == 1:
        for i in range(0, N):  # column
            for j in range(0, N-1):  # row
                if cp[j][i] == 0:
                    isMoved = True
                    cnt = count0(MAP, j, i, dx, dy)
                    for zero in range(0, cnt):
                        for k in range(j, N-1):
                            cp[k][i] = cp[k+1][i]
                        cp[N-1][i] = 0
                elif cp[j][i] == cp[j+1][i]:
                    isMoved = True
                    cp[j][i] += cp[j+1][i]
                    cp[j+1][i] = 0

    if dx == 0 and dy == -1:
        for i in range(0, N):  # column
            for j in range(N-1, 0, -1):  #row
                if cp[j][i] == 0:
                    isMoved = True
                    cnt = count0(MAP, j, i, dx, dy)
                    for zero in range(0, cnt):
                        for k in range(j, 0, -1):
                            cp[k][i] = cp[k-1][i]
                        cp[0][i] = 0
                elif cp[j][i] == cp[j-1][i]:
                    isMoved = True
                    cp[j][i] += cp[j-1][i]
                    cp[j-1][i] = 0

    if dx == 1 and dy == 0:
        for i in range(0, N):  # row
            for j in range(N-1, 0, -1):  # column
                if cp[i][j] == 0:
                    print(i, j)
                    isMoved = True
                    cnt = count0(MAP, i, j, dx, dy)
                    for zero in range(0, cnt):
                        print(cnt)
                        for k in range(j, 0, -1):
                            cp[i][k] = cp[i][k-1]
                        cp[i][0] = 0
                    print(str(cp))
                elif cp[i][j] == cp[i][j-1]:
                    isMoved = True
                    cp[i][j] += cp[i][j-1]
                    cp[i][j-1] = 0

    if dx == -1 and dy == 0:
        for i in range(0, N):  # row
            for j in range(0, N-1):  # column
                if cp[i][j] == 0:
                    isMoved = True
                    cnt = count0(MAP, i, j, dx, dy)
                    for zero in range(0, cnt):
                        for k in range(j, N-1):
                            cp[i][k] = cp[i][k+1]
                        cp[i][N-1] = 0
                elif cp[i][j] == cp[i][j+1]:
                    isMoved = True
                    cp[i][j] += cp[i][j+1]
                    cp[i][j+1] = 0
    print(str(cp), dx, dy)
    return isMoved, cp


def solve():
    while queue:
        maze, depth, moved = queue.pop(0)
        cp = list(map(list, copy.deepcopy(maze)))
        if depth == 5:
            maxSet.append(max(map(max(cp))))
            continue

        for i in range(4):
            isMoved, maze = move(cp, movement[i], movement[i], depth)
            print(depth, i)
            if isMoved:
                queue.append((tuple(map(tuple, maze)), depth+1, i))
        depth += 1
        print(str(queue))
#    print(max(maxSet))


move(MAP, 1, 0, 1)