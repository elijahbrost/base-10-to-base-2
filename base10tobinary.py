import math

g = 1573788

j = []

while g > 2:
    h = math.log(g)/math.log(2)
    j.append(int(h))
    g = 2**h-2**int(h)
# failed attempt at correcting for float point inaccuracy
if g >= 1:
    j.append(1)
else:
    j.append(0)

k = 0
l = []
while k < j[0]+1:
    l.append(0)
    k = k + 1

for i in j:
    l[i] = '1'

l.reverse()

m = ""
for i in l:
    m = m + str(i)
print(m)