n = int(input())
h=  n// 3600
p = (n-h*3600)//60
g = (n-h*3600- p*60)
print(h,":",p,":",g)