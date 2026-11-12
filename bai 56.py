import sys
du_lieu_vao = sys.stdin.read().split()
a = list(map(int, du_lieu_vao))
mang_khong_trung = list(set(a))
if len(mang_khong_trung) < 3:
    print("-")
else:
    mang_khong_trung.sort()
    print(mang_khong_trung[2])