m,n = map(int,input().split())
for i in range(m,n+1 ):
    so_lan = 0
    for j in range(1,i+1):
        if i% j == 0 :
            so_lan = so_lan + 1
    if so_lan == 2 :
        print(i,end=" ")