def convertDecimalToBinaricString(decimalToConvert):
    a = decimalToConvert
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
    return g

def convertArrayOfDecimalsToArrayOfBinaricStrings(arrayToConvert):
    arrayOfStringularBinaries = []
    for i in arrayToConvert:
        arrayOfStringularBinaries.append(convertDecimalToBinaricString(i))
    return arrayOfStringularBinaries

def convertBinaricStringToDecimal(binaricStringToConvert):
    a = binaricStringToConvert
    d = 0
    b = list(a)
    c = len(b)
    for i in b:
        if i == '1':
            d = d + 2**(c-1)
        c = c - 1
    return d

def convertArrayOfBinaricStringsToArrayOfDecimals(arrayToConvert):
    arrayOfDecimals = []
    for i in arrayToConvert:
        arrayOfDecimals.append(convertBinaricStringToDecimal(i))
    return arrayOfDecimals

print(convertDecimalToBinaricString(6666))
print(convertArrayOfDecimalsToArrayOfBinaricStrings([6, 66, 666]))
print(convertBinaricStringToDecimal("11111"))
print(convertArrayOfBinaricStringsToArrayOfDecimals(["1", "11", "111", "1111"]))