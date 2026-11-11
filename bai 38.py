k = int(input())
dem = 0
so_hien_tai = 2
while dem < k:
    lan_chia = 0
    for i in range(1, so_hien_tai + 1):
        if so_hien_tai % i == 0:
            lan_chia += 1
    if lan_chia == 2:
        print(so_hien_tai, end=" ")
        dem += 1
    so_hien_tai += 1