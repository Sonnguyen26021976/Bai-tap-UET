a = list(map(int, input().split()))
so_am = []
for x in a :
    if x < 0 :
        so_am.append(x)
if len(so_am) == 0 :
    print("-")
else:
    print(max(so_am))