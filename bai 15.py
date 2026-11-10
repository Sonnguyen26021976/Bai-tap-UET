a,b,c = map(int,input().split())
if a> 0 and b> 0 and c>0 and a+b > c and b+c > a and a+c > b :
    print("Day la 3 canh cua mot tam giac ")
    cv = (a+b+c)
    p = cv/2
    s=(p*(p-a)*(p-b)*(p-c))**0.5
    print(f'{cv:.2f} {s:.1f}')
else :
    print("Day khong la 3 canh cua mot tam giac ")