# functions
def toBaseTen(num):
    digits = [int(x) for x in str(num)]
    res = 0
    p = len(digits) - 1
    for digit in digits:
        res += int(digit) * int(b1)**p
        p -= 1
    print(res)

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
    print(ans)


b1 = input("Enter base of number: ")
num = input("Enter number: ")
print("") # create space

b2 = input("Enter base to be converted to: ")



# converting non-base 10 to base 10
if b2 == str(10) :
    toBaseTen(int(num))

# converting base 10 to non base 10
elif b2 == str(2) :
    toBaseTwo(int(num))

else :
    if b1 > b2 :
        print("Convert to decimal")
    if b1 > b2 :
        print("Convert to binary")


# converting base 10 to no-base 10

"""
-Divide the decimal number by the target base.
-Record the remainder.
-Use the quotient as the new number to divide.
-Repeat until the quotient is 0.
-Write the remainders in reverse order as the final result.

Converting 23 to base 2

23÷2=11 remainder 1
11÷2=5 remainder 1
5÷2=2 remainder 1
2÷2=1 remainder 0
1÷2=0 remainder 1

Result: 23=10111
"""

# Converting between two bases that arent base 2 or 10

"""
two ways to do this one way is to onvert to base 2 as an inermidiary
the other is to convert to base 10 as an inermidary

which one it goes to should be reiant on whichever one requires less computation/lighter computation
"""

