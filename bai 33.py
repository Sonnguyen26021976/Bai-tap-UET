m, n = map(int, input().split())
so_lan = 0
for i in range(m, n + 1):
    lan_chia = 0
    if i > 1:
        for j in range(1, i + 1):
            if i % j == 0:
                lan_chia = lan_chia + 1
        if lan_chia == 2:
            so_lan = so_lan + 1
print(so_lan)