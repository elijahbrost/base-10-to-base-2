a = "11111"
d = 0

b = list(a)

c = len(b)

for i in b:
    if i == '1':
        d = d + 2**(c-1)
    c = c - 1
print(d)