m,n = map(int,input().split())
tong = 0
so_dem = 0
for i in range(m,n+1 ):
    so_lan = 0
    for j in range(1,i+1):
        if i% j == 0 :
            so_lan = so_lan + 1
    if so_lan == 2 :
        tong = tong + i
        so_dem = so_dem + 1
ket_qua = tong/so_dem
print(f"{ket_qua:.2f}")