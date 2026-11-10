n = int(input())
if 0<n<=150 :
    if 0<n<=11:
        print("Thieu Nhi")
    if 11<n<= 25 :
        print("Thieu Nien")
    if 25<n<=50 :
        print("Trung Nien")
    if n>50:
        print("Cao nien ")
else :
    print("Yeu cau nhap dung so tuoi !")