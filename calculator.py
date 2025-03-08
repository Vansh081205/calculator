import math
print("*****WELCOME TO THE CALCULATOR*****\nBY-VANSH")
while True :
    a = float(input("ENTER FIRST NUMBER : "))
    b = float(input("ENTER SECOND NUMBER : "))
    sum = a+b
    diff = a-b
    product = a*b
    divide = a/b
    remainder = a%b
    roota= math.sqrt(a)
    rootb= math.sqrt(b)
    sina = math.sin(a)
    sinb = math.sin(b)
    cosa = math.cos(a)
    cosb = math.cos(b)
    tana = math.tan(a)
    tanb = math.tan(b)
    loga = math.log(a)
    logb = math.log(b)
    afact = math.factorial(int(a))
    bfact = math.factorial(int(b))
    pie = math.pi
    
    print("TO ADD : + ")
    print("TO SUBTRACT : - ")
    print("TO MULTIPLY : * ")
    print("TO DIVIDE : / ")
    print("FOR REMAINDER : % ")
    print("for sin of a: sina")
    print("for sin of b: sinb")
    print("for cos of a: cosa")
    print("for cos of b: cosb")
    print("for sq roota: roota")
    print("for sq rootb: rootb")
    print("for log of a : loga")
    print("for log of b : logb")
    print("to find factorial of a : afact")
    print("to find factorial of b : bfact")
    print("to find volume of square of side a: sqa")



    c = input("ENTER THE OPERATION YOU WANT TO PERFORM OR PRESS (Q) TO CLOSE :  ")

    if(c == "+"):
        print("SUM OF BOTH NUMBER IS",sum)
    elif(c== "-"):
        print("DIFFERENCE OF BOTH NUMBER IS",diff)
    elif(c== "*"):
        print("PRODUCT OF BOTH NUMBER IS",product)
    elif(c== "/"):
        print("DIVISION OF BOTH NUMBER IS",divide)
    elif(c == "%"):
        print("REMAINDER OF BOTH NUMBER IS",remainder)
    elif(c=="sina"):
        print("sin val of a :", sina )
    elif(c=="sinb"):
        print("sin val of b :", sinb)
    elif(c=="cosa"):
        print("cos val of a :", cosa)
    elif(c=="cosb"):
        print("cos val of b :", cosb)
    elif(c=="roota"):
        print("root of number is",roota)
    elif(c=="rootb"):
        print("root of number is",rootb)
    elif (c=="loga"):
        print("log value of a is:", loga)
    elif (c=="logb"):
        print("log value of b is:", logb)
    elif(c == "afact"):
        print("fact of a is :", afact)
    elif(c=="bfact"):
        print("factb is :", bfact)
    elif(c=="sqa"):
        print(4/3*pie*(a**a))
    elif(c == "Q"):
        print("*****CALCULATOR CLOSED*****")
    else:
        print("INVALID OUTPUT")

    print("*****THANKS FOR USING THE CALCULATOR*****")