from collections import deque


def bfs(start):
    visited[start] = True
    qu = deque()
    qu.append((start, 0))
    bacon_num = 0

    while qu:
        k, v = qu.popleft()

        for i in arr[k]:
            if not visited[i]:
                visited[i] = True
                qu.append((i, v + 1))
                bacon_num += v + 1

    return bacon_num


n, m = map(int, input().split())
arr = [list() for _ in range(n + 1)]
result = list()

for _ in range(m):
    i, j = (map(int, input().split()))
    arr[i].append(j)
    arr[j].append(i)


for i in range(1, n + 1):
    visited = [False for _ in range(n + 1)]
    result.append(bfs(i))

print(result.index(min(result)) + 1)