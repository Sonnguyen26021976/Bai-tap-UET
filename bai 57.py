import sys
du_lieu_vao = sys.stdin.read().split()
a = list(map(int, du_lieu_vao))
mang_khong_trung = set(a)
print(len(mang_khong_trung))