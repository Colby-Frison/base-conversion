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

# convert base 8 to base 16
def octaltoHexa(num):
    b1 = '8'
    b2 = '2'
    binary = octalToBinary(int(num))
    print(binary)
    b1 = '2'
    b2 = '16'
    print(binarytoHexa(binary))


# convert base 8 to base 16
def hexatoOcal(num):
    binary = hexatoBinary(num)
    print(binarytoOctal((hexatoBinary(num))))

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
print("") # create space

b2 = input("Enter base to be converted to: ")


if b2 == str(2) and b1 == str(8) :
    print(octalToBinary(int(num)))

elif b2 == str(2) and b1 == str(16) :
    print(hexatoBinary(num))

elif b2 == str(8) and b1 == str(2) :
    print(binarytoOctal(num))

elif b2 == str(16) and b1 == str(2) :
    print(binarytoHexa(num))

elif b2 == str(16) and b1 == str(8) :
    b1 = '8'
    b2 = '2'
    binary = octalToBinary(int(num))
    b1 = '2'
    b2 = '16'
    print(binarytoHexa(binary))

elif b2 == str(8) and b1 == str(16) :
    b1 = '16'
    b2 = '2'
    binary = hexatoBinary(num)
    b1 = '2'
    b2 = '8'
    print(binarytoOctal(binary))

# converting non-base 10 to base 10
elif b2 == str(10) :
    print(toBaseTen(int(num)))

# converting base 10 to non base 10
elif b1 == str(10) :
    print(fromBaseTen(int(num)))

else :
    print("bro")



# Converting between two bases that arent base 2 or 10

"""
two ways to do this one way is to onvert to base 2 as an inermidiary
the other is to convert to base 10 as an inermidary

which one it goes to should be reiant on whichever one requires less computation/lighter computation
"""

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