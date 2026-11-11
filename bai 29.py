n = int(input())
so_lan = 0
for i in range(1,n+1):
    if n % i == 0:
        so_lan = so_lan + 1
if so_lan == 2:
    print("Yes")
else :
    print("No")