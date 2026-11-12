m,n =  map(int,input().split())
a = list(map(int,input().split()))
found = False
for i in range(m):
    if n == a[i]:
        print("Yes")
        print(i)
        found = True
        break
if not found :
    print("No")