a, b, c = map(int, input().split())
cv = (a + b + c)
p = cv / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
r = (a * b * c) / (4 * s)
print(f'{r:.3f}')
