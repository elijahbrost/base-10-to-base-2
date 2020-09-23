p = [3]
e = p[-1]+1
while p[-1] < 100:
    if (e % 2) != 0:
        for i in p:
            if (e % i) != 0:
                if i == p[-1]:
                    p.append(e)
                    break
            else:
                break
    e = e+1
print(p)