import os
import time
import random

os.system("clear")

"""
Chapter 0
Quick Tricks:
Easy (and Impressive) Calculations
"""

def InstantMultiplication():
    """AB x 11 = A(A+B)B"""
    gen = random.randint(1, 99)

    start = time.time()
    print(f"{gen} * 11?\n")

    while True:
        try:
            ans = int(input())
            break
        except:
            continue

    correct = gen * 11
    
    if (correct != ans):
        print("Wrong!\n")
        print(f"Correct answer: {correct}")
        return False

    print("Good boi!\n")
    print(f"{round(time.time() - start, 2)} seconds! \n")
    return True

def SingleDigitSum():
    """Practice"""
    gen1 = random.randint(1, 9)
    gen2 = random.randint(1, 9)

    start = time.time()
    print(f"{gen1} + {gen2}?\n")

    while True:
        try:
            ans = int(input())
            break
        except:
            continue

    correct = gen1 + gen2

    if (correct != ans):
        print("Wrong!\n")
        print(f"Correct answer: {correct}")
        return False

    print("Good boi!\n")
    print(f"{round(time.time() - start, 2)} seconds! \n")
    return True

def SingleDigitSub():
    """Practice"""
    gen1 = random.randint(1, 9)
    gen2 = random.randint(1, 9)

    start = time.time()
    print(f"{gen1} - {gen2}?\n")
    
    while True:
        try:
            ans = int(input())
            break
        except:
            continue

    correct = gen1 - gen2

    if (correct != ans):
        print("Wrong!\n")
        print(f"Correct answer: {correct}")
        return False

    print("Good boi!\n")
    print(f"{round(time.time() - start, 2)} seconds! \n")
    return True

def SingleDigitProd():
    """Practice"""
    gen1 = random.randint(1, 9)
    gen2 = random.randint(1, 9)

    start = time.time()
    print(f"{gen1} * {gen2}?\n")

    while True:
        try:
            ans = int(input())
            break
        except:
            continue

    correct = gen1 * gen2

    if (correct != ans):
        print("Wrong!\n")
        print(f"Correct answer: {correct}")
        return False

    print("Good boi!\n")
    print(f"{round(time.time() - start, 2)} seconds! \n")
    return True

def TwoDigitSquare():
    """two-digit square that ends in five"""
    gen = int(str(random.randint(1, 9)) + "5")

    start = time.time()
    print(f"{gen} * {gen}?\n")

    while True:
        try:
            ans = int(input())
            break
        except:
            continue

    correct = gen * gen

    if (correct != ans):
        print("Wrong!\n")
        print(f"Correct answer: {correct}")
        return False
    
    print("Good boi!\n")
    print(f"{round(time.time() - start, 2)} seconds! \n")
    return True

def TwoDigitProd1():
    """Two-digit of the form AB * AC where B + C = 10."""
    temp = random.randint(1, 9)
    temp2 = random.randint(1, 9)
    gen1 = int(str(temp) + str(temp2))
    gen2 = int(str(temp) + str(10 - temp2))
    
    start = time.time()
    print(f"{gen1} * {gen2}?\n")

    while True:
        try:
            ans = int(input())
            break
        except:
            continue

    correct = gen1 * gen2

    if (correct != ans):
        print("Wrong!\n")
        print(f"Correct answer: {correct}")
        return False
    
    print("Good boi!\n")
    print(f"{round(time.time() - start, 2)} seconds! \n")
    return True

chapter0 = [
        InstantMultiplication,
        SingleDigitSum,
        SingleDigitSub,
        SingleDigitProd,
        TwoDigitSquare,
        TwoDigitProd1,
        ]

"""
Chapter 1
Quick Tricks:
Easy (and Impressive) Calculations
"""

def TwoDigitSum():
    """Practice"""
    gen1 = random.randint(10, 99)
    gen2 = random.randint(10, 99)

    start = time.time()
    print(f"{gen1} + {gen2}?\n")
    
    while True:
        try:
            ans = int(input())
            break
        except:
            continue

    correct = gen1 + gen2

    if (correct != ans):
        print("Wrong!\n")
        print(f"Correct answer: {correct}")
        return False
    
    print("Good boi!\n")
    print(f"{round(time.time() - start, 2)} seconds! \n")
    return True

def ThreeDigitSum():
    """Practice"""
    gen1 = random.randint(100, 999)
    gen2 = random.randint(100, 999)

    start = time.time()
    print(f"{gen1} + {gen2}?\n")

    while True:
        try:
            ans = int(input())
            break
        except:
            continue

    correct = gen1 + gen2

    if (correct != ans):
        print("Wrong!\n")
        print(f"Correct answer: {correct}")
        return False
    
    print("Good boi!\n")
    print(f"{round(time.time() - start, 2)} seconds! \n")
    return True

def TwoDigitSub():
    """Practice"""
    gen1 = random.randint(10, 99)
    gen2 = random.randint(10, 99)

    start = time.time()
    print(f"{gen1} - {gen2}?\n")

    while True:
        try:
            ans = int(input())
            break
        except:
            continue

    correct = gen1 - gen2

    if (correct != ans):
        print("Wrong!\n")
        print(f"Correct answer: {correct}")
        return False
    
    print("Good boi!\n")
    print(f"{round(time.time() - start, 2)} seconds! \n")
    return True

def ThreeDigitSub():
    """Practice"""
    gen1 = random.randint(100, 999)
    gen2 = random.randint(100, 999)

    start = time.time()
    print(f"{gen1} - {gen2}?\n")

    while True:
        try:
            ans = int(input())
            break
        except:
            continue

    correct = gen1 - gen2

    if (correct != ans):
        print("Wrong!\n")
        print(f"Correct answer: {correct}")
        return False
    
    print("Good boi!\n")
    print(f"{round(time.time() - start, 2)} seconds! \n")
    return True
    

chapter1 = [
    TwoDigitSum,
    ThreeDigitSum,
    TwoDigitSub,
    ThreeDigitSub,
]

"""
Chapter 2
Products of a Misspent Youth:
Basic Multiplication
"""

def TwoByOneMul():
    """2-By-1 Multiplication Problems"""
    gen1 = random.randint(1, 9)
    gen2 = random.randint(10, 99)

    start = time.time()
    print(f"{gen1} * {gen2}?\n")

    while True:
        try:
            ans = int(input())
            break
        except:
            continue

    correct = gen1 * gen2

    if (correct != ans):
        print("Wrong!\n")
        print(f"Correct answer: {correct}")
        return False
    
    print("Good boi!\n")
    print(f"{round(time.time() - start, 2)} seconds! \n")
    return True

def ThreeByOneMul():
    """3-By-1 Multiplication Problems"""
    gen1 = random.randint(1, 9)
    gen2 = random.randint(100, 999)

    start = time.time()
    print(f"{gen1} * {gen2}?\n")

    while True:
        try:
            ans = int(input())
            break
        except:
            continue

    correct = gen1 * gen2

    if (correct != ans):
        print("Wrong!\n")
        print(f"Correct answer: {correct}")
        return False
    
    print("Good boi!\n")
    print(f"{round(time.time() - start, 2)} seconds! \n")
    return True

def TwoDigitSquareAny():
    """Interesting property for square of two numbers"""
    gen = random.randint(10, 99)

    start = time.time()
    print(f"{gen}^2?\n")

    while True:
        try:
            ans = int(input())
            break
        except:
            continue

    correct = gen * gen

    if (correct != ans):
        print("Wrong!\n")
        print(f"Correct answer: {correct}")
        return False
    
    print("Good boi!\n")
    print(f"{round(time.time() - start, 2)} seconds! \n")
    return True

chapter2 = [
    TwoByOneMul,
    ThreeByOneMul,
    TwoDigitSquareAny
]

def TwoByTwoMul():
    """Multiplying two digit numbers"""
    gen1 = random.randint(10, 99)
    gen2 = random.randint(10, 99)

    start = time.time()
    print(f"{gen1} * {gen2}?\n")

    while True:
        try:
            ans = int(input())
            break
        except:
            continue

    correct = gen1 * gen2

    if (correct != ans):
        print("Wrong!\n")
        print(f"Correct answer: {correct}")
        return False
    
    print("Good boi!\n")
    print(f"{round(time.time() - start, 2)} seconds! \n")
    return True

chapter3 = [
    TwoByTwoMul
]

"""
Chapter 7
A Memorable Chapter:
Memorizing Numbers:
"""

def ThePhoneticCode():
    "This can be hard to remember"
    codes = [
        ["t or d sound?", 1],
        ["n sound", 2],
        ["m sound", 3],
        ["r sound", 4],
        ["l sound", 5],
        ["j, ch, sh sound", 6],
        ["k or hard g sound", 7],
        ["f or v sound", 8],
        ["p or b sound", 9],
        ["z or s sound", 0]
    ]

    code = codes[random.randint(0, len(codes) - 1)]

    prompt, correct = code[0], code[1]
    
    print(f"{prompt}?\n")

    while True:
        try:
            ans = int(input())
            break
        except:
            continue

    if (correct != ans):
        print("Wrong!\n")
        print(f"Correct answer: {correct}")
        return False
    
    print("Good boi!\n")
    return True

chapter7 = [
    ThePhoneticCode
]

while True:
    # fn = chapter0[random.randint(0, len(chapter0) - 1)]
    # fn = chapter1[random.randint(0, len(chapter1) - 1)]
    # fn = chapter2[random.randint(0, len(chapter2) - 1)]
    # fn = chapter3[random.randint(0, len(chapter3) - 1)]
    
    # fn = chapter7[random.randint(0, len(chapter3) - 1)]

    # everything = chapter0 + chapter1 + chapter2 + chapter3
    # fn = everything[random.randint(0, len(everything) - 1)]

    some = chapter2 + chapter3
    fn = some[random.randint(0, len(some) - 1)]

    if not fn():
        break

    input("Press any key to continue")
    os.system("clear")
    
