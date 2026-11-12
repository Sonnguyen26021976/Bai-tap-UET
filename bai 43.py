n= int(input())
a = list(map(int, input().split()))
tong_so = 0
for i in (a):
    if i % 2 == 0 :
        tong_so = tong_so + 1
print(tong_so)