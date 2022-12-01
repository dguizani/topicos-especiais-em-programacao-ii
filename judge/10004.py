# exec -> python judge/10004.py < judge/10004ex.txt > judge/10004out.txt

from collections import deque


while (N := int(input())) != 0:
    M = int(input())
    
    graph = [[0] * N for _ in range(N)]
    color = [-1] * N

    for _ in range(M):
        a, b = [int(x) for x in input().split()]
        graph[a][b] = 1
        graph[b][a] = 1

    queue = deque([0])
    
    color[0] = 0
    flag = True

    while queue:
        u = queue.popleft()
        
        for v in range(N):
            if not graph[u][v]:
                continue
            
            if color[v] == -1:
                color[v] = color[u] + 1
                queue.append(v)

            elif color[u] == color[v]:
                flag = False
                break
        
        if not flag:
            break

    if flag:
        print("BICOLORABLE.")
    else:
        print("NOT BICOLORABLE.")
