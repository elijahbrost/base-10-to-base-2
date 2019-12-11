a = 6666

b = []
c = 0

d = 1

e = 0

f = []

g = ""

while a > 0:
    while a >= d:
        if a <= 3:
            c = a
            d = d * 4
        else:
            c = c + 1
            d = d * 2
    if a != d:
        a = int(a - (d/2))
    b.append(c)
    c = 0
    d = 1

while e < b[0]:
    f.append(0)
    e = e + 1
    
for i in b:
    f[i-1] = 1

f.reverse()
for i in f:
    g = g + str(i)
print(g)
