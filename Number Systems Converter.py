import time

# functions converting number systems
def de_to_bi(x):
    a = x
    l = []
    for i in range(a):
        k = a % 2
        j = a // 2
        a = j
        l.append(k)
        if a == 0: 
            break
    s = ""
    for i in l[::-1]:
        s += str(i)
    print("""
The decimal number""", x, "to binary is", str(s) + ".")

def de_to_oct(x):
    a = x
    l = []
    for i in range(a):
        k = a % 8
        j = a // 8
        a = j
        l.append(k)
        if a == 0: 
            break
    s = ""
    for i in l[::-1]:
        s += str(i)
    print("""
The decimal number""", x, "to octal is", str(s) + ".")

def de_to_hex(x):
    a = x
    l = []
    for i in range(a):
        k = a % 16
        j = a // 16
        a = j
        if k <= 9:
            l.append(k)
        elif k == 10:
            l.append('A')
        elif k == 11:
            l.append('B')
        elif k == 12:
            l.append('C')
        elif k == 13:
            l.append('D')
        elif k == 14:
            l.append('E')
        elif k == 15:
            l.append('F')
        if a == 0: 
            break
    s = ""
    for i in l[::-1]:
        s += str(i)
    print("""
The decimal number""", x, "to hexadecimal is", str(s) + ".")

def bi_to_de(x):
    r = len(str(x))
    s = 0
    for i in range(r):
        s += int(str(x)[-(i + 1)]) * (2 ** i)
    print("""
The binary number""", x, "to decimal is", str(s) + ".")

def oct_to_de(x):
    r = len(str(x))
    s = 0
    for i in range(r):
        s += int(str(x)[-(i + 1)]) * (8 ** i)
    print("""
The octal number""", x, "to decimal is", str(s) + ".")

def hex_to_de(x):
    r = len(str(x))
    s = 0
    y = str(x).casefold()
    for i in range(r):
        if y[-(i + 1)] == 'A'.casefold():
            s += 10 * (16 ** i)
        elif y[-(i + 1)] == 'B'.casefold():
            s += 11 * (16 ** i)
        elif y[-(i + 1)] == 'C'.casefold():
            s += 12 * (16 ** i)
        elif y[-(i + 1)] == 'D'.casefold():
            s += 13 * (16 ** i)
        elif y[-(i + 1)] == 'E'.casefold():
            s += 14 * (16 ** i)
        elif y[-(i + 1)] == 'F'.casefold():
            s += 15 * (16 ** i)
        elif int(str(x)[-(i + 1)]) <= 9:
            s += int(str(x)[-(i + 1)]) * (16 ** i)
    print("""
The hexadecimal number""", x.upper(), "to decimal is", str(s) + ".")

def bi_to_oct(x):
    r = len(str(x))
    y = 0
    for i in range(r):
        y += int(str(x)[-(i + 1)]) * (2 ** i)
    l = []
    for i in range(y):
        k = y % 8
        j = y // 8
        y = j
        l.append(k)
        if y == 0: 
            break
    s = ""
    for i in l[::-1]:
        s += str(i)
    print("""
The binary number""", x, "to octal is", str(s) + ".")

def bi_to_hex(x):
    r = len(str(x))
    s = 0
    for i in range(r):
        s += int(str(x)[-(i + 1)]) * (2 ** i)
    l = []
    for i in range(s):
        k = s % 16
        j = s // 16
        s = j
        if k <= 9:
            l.append(k)
        elif k == 10:
            l.append('A')
        elif k == 11:
            l.append('B')
        elif k == 12:
            l.append('C')
        elif k == 13:
            l.append('D')
        elif k == 14:
            l.append('E')
        elif k == 15:
            l.append('F')
        if s == 0: 
            break
    w = ""
    for i in l[::-1]:
        w += str(i)
    print("""
The binary number""", x, "to hexadecimal is", str(w) + ".")

def oct_to_bi(x):
    r = len(str(x))
    y = 0
    for i in range(r):
        y += int(str(x)[-(i + 1)]) * (8 ** i)
    l = []
    for i in range(y):
        k = y % 2
        j = y // 2
        y = j
        l.append(k)
        if y == 0: 
            break
    s = ""
    for i in l[::-1]:
        s += str(i)
    print("""
The octal number""", x, "to binary is", str(s) + ".")

def oct_to_hex(x):
    r = len(str(x))
    s = 0
    for i in range(r):
        s += int(str(x)[-(i + 1)]) * (8 ** i)
    l = []
    for i in range(s):
        k = s % 16
        j = s // 16
        s = j
        if k <= 9:
            l.append(k)
        elif k == 10:
            l.append('A')
        elif k == 11:
            l.append('B')
        elif k == 12:
            l.append('C')
        elif k == 13:
            l.append('D')
        elif k == 14:
            l.append('E')
        elif k == 15:
            l.append('F')
        if s == 0: 
            break
    w = ""
    for i in l[::-1]:
        w += str(i)
    print("""
The octal number""", x, "to hexadecimal is", str(w) + ".")

def hex_to_bi(x):
    r = len(str(x))
    s = 0
    y = str(x).casefold()
    for i in range(r):
        if y[-(i + 1)] == 'A'.casefold():
            s += 10 * (16 ** i)
        elif y[-(i + 1)] == 'B'.casefold():
            s += 11 * (16 ** i)
        elif y[-(i + 1)] == 'C'.casefold():
            s += 12 * (16 ** i)
        elif y[-(i + 1)] == 'D'.casefold():
            s += 13 * (16 ** i)
        elif y[-(i + 1)] == 'E'.casefold():
            s += 14 * (16 ** i)
        elif y[-(i + 1)] == 'F'.casefold():
            s += 15 * (16 ** i)
        elif int(str(x)[-(i + 1)]) <= 9:
            s += int(str(x)[-(i + 1)]) * (16 ** i)
    l = []
    for i in range(s):
        k = s % 2
        j = s // 2
        s = j
        l.append(k)
        if s == 0: 
            break
    w = ""
    for i in l[::-1]:
        w += str(i)
    print("""
The hexadecimal number""", x.upper(), "to binary is", str(w) + ".")

def hex_to_oct(x):
    r = len(str(x))
    s = 0
    y = str(x).casefold()
    for i in range(r):
        if y[-(i + 1)] == 'A'.casefold():
            s += 10 * (16 ** i)
        elif y[-(i + 1)] == 'B'.casefold():
            s += 11 * (16 ** i)
        elif y[-(i + 1)] == 'C'.casefold():
            s += 12 * (16 ** i)
        elif y[-(i + 1)] == 'D'.casefold():
            s += 13 * (16 ** i)
        elif y[-(i + 1)] == 'E'.casefold():
            s += 14 * (16 ** i)
        elif y[-(i + 1)] == 'F'.casefold():
            s += 15 * (16 ** i)
        elif int(str(x)[-(i + 1)]) <= 9:
            s += int(str(x)[-(i + 1)]) * (16 ** i)
    l = []
    for i in range(s):
        k = s % 8
        j = s // 8
        s = j
        l.append(k)
        if s == 0: 
            break
    w = ""
    for i in l[::-1]:
        w += str(i)
    print("""
The hexadecimal number""", x.upper(), "to octal is", str(w) + ".")

# the first input: which number system to convert from
wanna_go = ""

num_sys1 = input("""Hi! Welcome to the number system converter program!

Which number system would you like to convert from? (choose between binary, octal, decimal, and hexadecimal): """)

# while loop so that the program can be rerun unless told not to
while wanna_go.casefold() != 'no':

# limit the first input to 'binary,' 'octal,' 'decimal,' or 'hexadecimal'
    while num_sys1.casefold() != 'binary' and num_sys1.casefold() != 'octal' and num_sys1.casefold() != 'decimal' and num_sys1.casefold() != 'hexadecimal':
        num_sys1 = input("""
You must choose between binary, octal, decimal, and hexadecimal.
Please try again: """)

    not_num = ""

    if num_sys1.casefold() == 'binary':
        not_num = 'octal, decimal, and hexadecimal'
    elif num_sys1.casefold() == 'octal':
        not_num = 'binary, decimal, and hexadecimal'
    elif num_sys1.casefold() == 'decimal':
        not_num = 'binary, octal, and hexadecimal'
    elif num_sys1.casefold() == 'hexadecimal':
        not_num = 'binary, octal, and decimal'

# the second input: which number system to convert into
    num_sys2 = input("""
Thanks for the input!
Which number system would you like to convert it into? (choose between """ + not_num + "): ")

# limit the second input to the number systems excluding the one chosen in the first input
    while (num_sys2.casefold() == num_sys1.casefold()) or (num_sys2.casefold() != 'binary' and num_sys2.casefold() != 'octal' and num_sys2.casefold() != 'decimal' and num_sys2.casefold() != 'hexadecimal'):
        if num_sys2.casefold() == num_sys1.casefold():
            num_sys2 = input("""
You cannot choose """ + num_sys1.casefold() + """ again.
Please try again: """)
        elif num_sys2.casefold() != 'binary' or 'octal' or 'decimal' or 'hexadecimal':
            num_sys2 = input("""
Please choose between """ + not_num + """.
Try again: """)

# the third input: the number
    x = input("""
Type in a """ + num_sys1.casefold() + " number: ")

# check and limit that the number (third input) is a number of the number system being converted from (first input)
    if num_sys1.casefold() == 'binary':
        y = 'hmm'
        while y == 'hmm':
            try:
                int(x, 2)
                break
            except ValueError:
                x = input("""
Please type in a binary number!
Try again: """)

    if num_sys1.casefold() == 'octal':
        y = 'hmm'
        while y == 'hmm':
            try:
                int(x, 8)
                break
            except ValueError:
                x = input("""
Please type in an octal number!
Try again: """)

    if num_sys1.casefold() == 'decimal':
        y = 'hmm'
        while y == 'hmm':
            try:
                int(x, 10)
                break
            except ValueError:
                x = input("""
Please type in an decimal number!
Try again: """)

    if num_sys1.casefold() == 'hexadecimal':
        y = 'hmm'
        while y == 'hmm':
            try:
                int(x, 16)
                break
            except ValueError:
                x = input("""
Please type in a hexadecimal number!
Try again: """)

# convert the number (third input) to the wanted number system (second input)
    if num_sys1.casefold() == 'binary' and num_sys2.casefold() == 'decimal':
        bi_to_de(int(x))
    elif num_sys1.casefold() == 'binary' and num_sys2.casefold() == 'octal':
        bi_to_oct(x)
    elif num_sys1.casefold() == 'binary' and num_sys2.casefold() == 'hexadecimal':
        bi_to_hex(x)
    
    elif num_sys1.casefold() == 'decimal' and num_sys2.casefold() == 'binary':
        de_to_bi(int(x))
    elif num_sys1.casefold() == 'decimal' and num_sys2.casefold() == 'octal':
        de_to_oct(int(x))
    elif num_sys1.casefold() == 'decimal' and num_sys2.casefold() == 'hexadecimal':
        de_to_hex(int(x))
    
    elif num_sys1.casefold() == 'octal' and num_sys2.casefold() == 'decimal':
        oct_to_de(int(x))
    elif num_sys1.casefold() == 'octal' and num_sys2.casefold() == 'binary':
        oct_to_bi(x)
    elif num_sys1.casefold() == 'octal' and num_sys2.casefold() == 'hexadecimal':
        oct_to_hex(x)

    elif num_sys1.casefold() == 'hexadecimal' and num_sys2.casefold() == 'binary':
        hex_to_bi(x)
    elif num_sys1.casefold() == 'hexadecimal' and num_sys2.casefold() == 'decimal':
        hex_to_de(x)
    elif num_sys1.casefold() == 'hexadecimal' and num_sys2.casefold() == 'octal':
        hex_to_oct(x)

# ask whether to exit the program or not
    wanna_go = input("""
Would you like to convert again? (yes or no): """)

    while wanna_go.casefold() != 'yes' and wanna_go.casefold() != 'no':
        wanna_go = input("""
Please type either 'yes' or 'no': """)

    if wanna_go.casefold() == 'no':
        break

    num_sys1 = input("""------------------------------------------------------------
Here we go again!

Which number system would you like to convert from? (choose between binary, octal, decimal, and hexadecimal): """)

print("""
See you next time!""")

# exit program after three seconds
time.sleep(3)
