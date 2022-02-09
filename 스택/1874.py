N = int(input())
seq = []
for i in range(N):
    seq.append(int(input()))

stack = []
operation = []


def solve():
    for i in range(N):
        stack.append(i+1)
        operation.append('+')
        while stack[-1] == seq[0]:
            seq.pop(0)
            stack.pop()
            operation.append('-')
            if not stack:
                break

    if stack:
        print('NO')
    else:
        print('\n'.join(operation))

solve()