a,b,c = map(int,input().split())
cv = (a+b+c)
p = cv/2
s=(p*(p-a)*(p-b)*(p-c))**0.5
print(f'{cv:.1f} {s:.3f}')