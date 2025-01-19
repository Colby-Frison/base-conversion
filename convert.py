# functions

# converting to base 10
def toBaseTen(num):
    digits = [int(x) for x in str(num)]
    res = 0
    p = len(digits) - 1
    for digit in digits:
        res += int(digit) * int(b1)**p
        p -= 1
    return res

# converting from base 10
def fromBaseTen(num):
    res = []
    
    while num != 0 :
        r = num % int(b2)
        res.append(int(r))
        num -= r
        num /= int(b2)
    ans = ""
    res.reverse()
    for x in res:
        if x > 9 :
            ans += numberToLetter(x)
        else :
            ans += str(x)
    return ans

def hextoTen(num):
    temp = list(num)
    i = 0
    digits = []
    while i < len(temp) :
        if temp[i].isdigit() :
            digits.append(int(temp[i]))
        else :
            digits.append(int(letterToNumber(temp[i])))
        i += 1
    res = 0
    p = len(digits) - 1
    for digit in digits:
        res += int(digit) * 16**p
        p -= 1
    return res

# convert base 8 to base 2
def octalToBinary(num):
    digits = [int(x) for x in str(num)]
    res = []
    for digit in digits:

        res += fromBaseTen(digit).zfill(3)
    ans = ""
    while res[0] == str(0) :
        res.pop(0)
    for x in res:
        ans += str(x)
    return ans

# convert base 16 to base 2
def hexatoBinary(num):
    temp = list(num)
    i = 0
    digits = []
    while i < len(temp) :
        if temp[i].isdigit() :
            digits.append(int(temp[i]))
        else :
            digits.append(int(letterToNumber(temp[i])))
        i += 1
    res = []
    for digit in digits:
        res += fromBaseTen(digit).zfill(4)
    ans = ""
    while res[0] == str(0) :
        res.pop(0)
    for x in res:
        ans += str(x)
    return ans

# convert base 2 to base 8
def binarytoOctal(num):
    num = num[::-1]
    temp = [num[i:i+3] for i in range(0, len(num), 3)]
    groups = []
    for x in temp :
        groups.append(x[::-1])
    groups.reverse()

    res = ""
    for x in groups:
        res += str(toBaseTen(x))
    return res

# convert base 2 to base 16
def binarytoHexa(num):
    num = num[::-1]
    temp = [num[i:i+4] for i in range(0, len(num), 4)]
    groups = []
    for x in temp :
        groups.append(x[::-1])
    groups.reverse()

    res = ""
    for x in groups:
        y = toBaseTen(x)
        if y <= 9:
            res += str(y)
        else :
            res += numberToLetter(y)
    return res

#------------------------------------------------------------#
# number <-> letter

# Convert letter to number
def letterToNumber(x):
    switcher = {
        "A": "10",
        "B": "11",
        "C": "12",
        "D": "13",
        "E": "14",
        "F": "15",
    }

    return switcher.get(x, "nothing")

# Convert letter to number
def numberToLetter(x):
    switcher = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }

    return switcher.get(x, "nothing")


##############################################################

b1 = input("Enter base of number: ")
num = input("Enter number: ")

if '.' in num:
    print("decimal not supported")
    num = input("Enter number: ")

print("") # create space


# Converts binary to all other
if b1 == str(2):
    print("Binary: " + num)
    b2 = '8'
    print("Octal: " + str(binarytoOctal(num)))
    b2 = '10'
    print("Decimal: " + str(toBaseTen(int(num))))
    b2 = '16'
    print("Hex: " + str(binarytoHexa(num)))

# Converts Octal to all other
elif b1 == str(8):
    b2 = '2'
    print("Binary: " + str(octalToBinary(int(num))))
    print("Octal: " + num)
    b2 = '10'
    print("Decimal: " + str(toBaseTen(int(num))))
    b1 = '8'
    b2 = '2'
    binary = octalToBinary(int(num))
    b1 = '2'
    b2 = '16'
    print("Hex: " + str(binarytoHexa(binary)))

# Converts decimal to all other
elif b1 == str(10):
    b2 = '2'
    print("Binary: " + fromBaseTen(int(num)))
    b2 = '8'
    print("Octal: " + fromBaseTen(int(num)))
    print("Decimal: " + num)
    b2 = '16'
    print("Hex: " + fromBaseTen(int(num)))

# Converts hex to all other
elif b1 == str(16):
    b2 = '2'
    binary = hexatoBinary(num)
    print("Binary: " + str(binary))
    b1 = '2'
    b2 = '8'
    print("Octal: " + str(binarytoOctal(binary)))
    b2 = '10'
    print("Decimal: " + str(hextoTen(num)))
    b2 = '16'
    print("Hex: " + num)

else :
    print("bro")

"""
Check list

[x] From base 10
[x] To base to
[ ] Floating point decimal to binary
[x] Octal to binary
[x] hexadecimal to binary
[x] Decimal to octal
[x] Decimal to Hecadecimal
[x] Binary to Octal
[x] Binary to hexadecimal
[x] Octal to hexadecimal
[x] Hexadecimal to Octal



"""