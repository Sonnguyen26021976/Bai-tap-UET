def kiem_tra_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
a = list(map(int, input().split()))
so_nguyen_to = []
tong = 0
for x in a:
    if kiem_tra_nguyen_to(x):
        so_nguyen_to.append(x)
        tong += x
if len(so_nguyen_to) > 0:
    print(*so_nguyen_to)
else:
    print("-")

print(tong)