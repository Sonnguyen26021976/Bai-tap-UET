n = int(input())
a = list(map(int, input().split()))
tong_so = 0
for i in range(n):
    if i % 2 == 0 :
        tong_so = tong_so + a[i]
print(tong_so)