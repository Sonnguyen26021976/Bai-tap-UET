n = int(input())
so_uoc = 0
for i in range(1, n + 1):
    if n% i == 0 :
        so_uoc = so_uoc + 1
print(so_uoc)