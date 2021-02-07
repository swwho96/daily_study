# 스택구조
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.pop()
stack.append(4)
print(stack)
print(stack[::-1])

# 큐 구조
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
queue.append(4)
print(list(queue))

# 재귀함수
def infinity(count):
    print("재귀함수를 호출하고 있습니다.", count)
    infinity(count+1)

infinity(0)

# 재귀함수 호출 종료
def infinity_exit(i):
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
    infinity_exit(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')

infinity_exit(1)

# 팩토리얼 구현
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_reculsive(n):
    if n <= 1:
        return 1
    return n * factorial_reculsive(n-1)

# DFS
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * 9
dfs(graph, 1, visited)

# BFS
from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
visited = [False] * 9
bfs(graph, 1, visited)

N, M = map(int, input().split())
basket = []
for i in range(N):
    basket.append(list(map(int, input())))

def find_holl(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if basket[x][y] == 0:
        basket[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if find_holl(i,j) == True:
            result += 1
print(result)

from collections import deque
N, M = map(int, input().split())
Map = []
for i in range(N):
    Map.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def Map_escape(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if Map[nx][ny] == 0:
                continue
            if Map[nx][ny] == 1:
                Map[nx][ny] = Map[x][y] + 1
                queue.append((nx, ny))
    return Map[N-1][M-1]

print(Map_escape(0,0))