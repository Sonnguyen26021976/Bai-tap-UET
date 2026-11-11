n = int(input())
if 0<=n<=1 :
    print(n*12000)
elif 1< n <= 30 :
    print(12000 + (n-1)*10000)
else :
    print(12000 + 10000*29 + (n-30)*9000)
