m,n = map(int,input().split())
so_lan = 0
tong = 0
for i in range(m,n+1):
    if i % 3 == 0 or i % 5 == 0:
        so_lan = so_lan + 1
    if i % 2 == 0 :
        tong = tong + i
print(so_lan,tong)