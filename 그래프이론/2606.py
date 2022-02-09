N = int(input())
M = int(input())
ADJ = [[0]*N for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    ADJ[a-1][b-1] = 1
    ADJ[b-1][a-1] = 1
queue = []
visited = [0]*N


def solve():
    visited[0] = 1
    queue.append(0)
    count = 0

    while queue:
        h = queue.pop(0)
        count += 1
        for i in range(N):
            if visited[i] == 0 and ADJ[h][i] == 1:
                visited[i] = 1
                queue.append(i)
    print(count-1)


solve()