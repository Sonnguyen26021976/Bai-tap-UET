n = int(input())
a = list(map(int, input().split()))
so_duong = []
so_am = []
for i in a:
    if i > 0:
        so_duong.append(i)
    elif i < 0:
        so_am.append(i)
print(len(so_duong), len(so_am))
if len(so_duong) > 0:
    print(*so_duong)
else:
    print("-")
if len(so_am) > 0:
    print(*so_am)
else:
    print("-")