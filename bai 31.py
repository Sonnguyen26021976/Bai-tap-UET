m, n = map(int, input().split())
so_lan = 0
for i in range(m,n+1):
    if i % 3 == 0 :
        so_lan = so_lan + 1
print(so_lan)
