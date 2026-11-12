n = int(input())
a = list(map(int, input().split()))
max = a[0]
vi_tri = 0
for i in range(n):
    if max < a[i] :
        max = a[i]
        vi_tri = i
print(max,vi_tri)