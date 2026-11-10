n = int(input())
hang_don_vi = n % 10
hang_chuc = (n // 10) % 10
hang_tram = (n // 100) % 10
hang_nghin = (n // 1000) % 10
hang_chuc_nghin = (n // 10000) % 10
tong = hang_chuc_nghin + hang_nghin + hang_tram + hang_chuc + hang_don_vi
nut = tong % 10
if nut == 9:
    print(nut)
    print("May Man")
else:
    print(nut)
    print("Chua may man")