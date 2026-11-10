a,b = map(float,input().split())
c = (a+b*2)/3
print(f'{c:.1f}')
if c>=8 :
    print("Gioi")
if 8>c>=6.5:
    print("Kha")
if 6.5>c>=5:
    print("Trung Binh")
if 5>c>=3.5:
    print("Yeu")
if 3.5>c :
    print("kem")