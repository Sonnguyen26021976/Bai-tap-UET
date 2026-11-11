t, m = map(int, input().split())
for i in range(1, min(t, m) + 1):
    if t % i == 0 and m % i == 0:
        ucln = i
print(f"{t // ucln}/{m // ucln}")