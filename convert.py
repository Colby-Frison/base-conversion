# functions

# converting non-base 10 to base 10
def toBaseTen(num):
    digits = [int(x) for x in str(num)]
    res = 0
    p = len(digits) - 1
    for digit in digits:
        res += int(digit) * int(b1)**p
        p -= 1
    return res

# converting base 10 to no-base 10
def toBaseTwo(num):
    res = []
    
    while num != 0 :
        r = num % 2
        res.append(int(r))
        num -= r
        num /= 2
    ans = ""
    res.reverse()
    for x in res:
        ans += str(x)
    return ans

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

#
def octalToBinary(num):
    digits = [int(x) for x in str(num)]
    res = []
    for digit in digits:

        res += toBaseTwo(digit).zfill(3)
    ans = ""
    if res[0] == str(0) :
        res.pop(0)
    for x in res:
        ans += str(x)
    print(ans)

##############################################################

b1 = input("Enter base of number: ")
num = input("Enter number: ")
print("") # create space

b2 = input("Enter base to be converted to: ")


if b2 == str(2) and b1 == str(8) :
    octalToBinary(int(num))

# converting non-base 10 to base 10
elif b2 == str(10) :
    print(toBaseTen(int(num)))

# converting base 10 to non base 10
elif b2 == str(2) :
    print(toBaseTwo(int(num)))


else :
    if b1 > b2 :
        print("Convert to decimal")
    if b1 > b2 :
        print("Convert to binary")



# Converting between two bases that arent base 2 or 10

"""
two ways to do this one way is to onvert to base 2 as an inermidiary
the other is to convert to base 10 as an inermidary

which one it goes to should be reiant on whichever one requires less computation/lighter computation
"""

