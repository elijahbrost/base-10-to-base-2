def convertDecimalToBinaricString(decimalToConvert):
    decimalToConvert = decimalToConvert
    arrayOfStringularBinaries = []
    greatestRoundComponent = 1
    lengthOfBinary = 1
    while greatestRoundComponent*2 < decimalToConvert:
        lengthOfBinary = lengthOfBinary+1
        greatestRoundComponent = greatestRoundComponent*2
    if greatestRoundComponent*2 == decimalToConvert:
        greatestRoundComponent = decimalToConvert
        lengthOfBinary = lengthOfBinary+1
    while lengthOfBinary > 0:
        arrayOfStringularBinaries.append("0")
        lengthOfBinary = lengthOfBinary-1
    arrayOfStringularBinaries[0] = "1"
    decimalToConvert = decimalToConvert - greatestRoundComponent
    position = 0
    while decimalToConvert > 0:
        if decimalToConvert < greatestRoundComponent:
            greatestRoundComponent = greatestRoundComponent/2
            if greatestRoundComponent > decimalToConvert:
                position = position+1
            else:
                position = position+1
                arrayOfStringularBinaries[position] = "1"
                decimalToConvert = decimalToConvert - greatestRoundComponent
    stringularBinary = ""
    for i in arrayOfStringularBinaries:
        stringularBinary = stringularBinary + str(i)
    return stringularBinary

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

print(convertDecimalToBinaricString(5))
print(convertArrayOfDecimalsToArrayOfBinaricStrings([3, 5, 7, 11, 13, 17]))
print(convertBinaricStringToDecimal("11111"))
print(convertArrayOfBinaricStringsToArrayOfDecimals(["1", "11", "111", "1111"]))
