from heapq import heappush, heappop

n = int(input())
m = int(input())
data = [[] for _ in range(m+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    data[a].append([b, c])
start, end = map(int, input().split())

INF = 1e9
dp = [INF]*(n+1)
heap = []
path = [0]*(n+1)

dp[start] = 0
heappush(heap, [0, start])
while heap:
    w, n = heappop(heap)
    for n_n, wei in data[n]:
        n_w = wei + w
        if n_w < dp[n_n]:
            dp[n_n] = n_w
            path[n_n] = n
            heappush(heap, [n_w, n_n])
            
print(dp[end])
ret = [end]
while True:
    ret.insert(0, path[ret[0]])
    if ret[0] == 1:
        break
print(len(ret))
print(' '.join(map(str, ret)))