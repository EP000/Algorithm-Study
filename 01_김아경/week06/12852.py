N = int(input())

count = [100000] * (N+1) # 인덱스를 만드는 횟수
count[1] = 0 # 1을 만드는 횟수는 0 (시작점이 1)
past = [0] * (N+1)

# 1부터 숫자 키워가면서 N 만들기
for i in range(1, N+1):
    
    if i*3 <= N and count[i*3] > count[i] + 1: 
    # 3 곱한 값이 N보다 작고 i 만드는 횟수가 더 작으면
        count[i*3] = count[i] + 1 # i 만드는 최소 횟수로 업데이트
        past[i*3] = i # i*3을 하기 전 값. 어떤 값을 넣어서 i*3을 만들었는지
    
    # 위와 동일
    if i*2 <= N and count[i*2] > count[i] + 1:
        count[i*2] = count[i] + 1
        past[i*2] = i
    
    if i+1 <= N and count[i+1] > count[i] + 1:
        count[i+1] = count[i] + 1
        past[i+1] = i
        
print(count[N])
while True:
    print(N, end = ' ')
    if N == 1:
        break
    N = past[N]