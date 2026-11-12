n = int(input())
a = list(map(int, input().split()))
so_chia = []
tong = 0
for i in (a) :
    if i% 5 == 0 :
        so_chia.append(i)
        tong += 1
if len(so_chia) >0 :
    print(*so_chia)
else :
    print("-")
print(tong)