N, M, H = map(int, input().split())
ADJ = [[0]*N for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    ADJ[a-1][b-1] = 1
    ADJ[b-1][a-1] = 1

checked1 = [0]*N
checked2 = [0]*N

queue = []


def DFS(head):
    checked1[head] = 1
    print(head+1, end=" ")
    for i in range(0, N):
        if checked1[i] == 0 and ADJ[head][i] == 1:
            DFS(i)


def BFS():
    queue.append(H-1)
    checked2[H-1] = 1

    while queue:
        h = queue.pop(0)
        print(h+1, end=" ")
        for i in range(0, N):
            if checked2[i] == 0 and ADJ[h][i] == 1:
                queue.append(i)
                checked2[i] = 1


def solve():
    DFS(H-1)
    print()
    BFS()


solve()