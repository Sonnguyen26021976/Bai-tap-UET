n = int(input())
tien_5k= n//5000
tien_2k = (n-tien_5k*5000)//2000
tien_1k = (n-tien_2k*2000-tien_5k*5000)//1000
print(tien_5k,tien_2k,tien_1k)