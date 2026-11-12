a = list(map(int, input().split()))
mang_khong_trung = list(set(a))
if len(mang_khong_trung) < 2:
    print("-")
else:
    so_lon_nhat = max(mang_khong_trung)
    mang_khong_trung.remove(so_lon_nhat)
    print(max(mang_khong_trung))