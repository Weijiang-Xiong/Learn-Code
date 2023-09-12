""" 
    According to https://docs.python.org/3/reference/compound_stmts.html, 
    while and for statement can have `else` clause.
"""

a = 1
while a < 3:
    print("a = {}".format(a))
    a += 1
    continue 
else:
    print("loop completed successfully")

b = 1
while b < 3:
    print("b = {}".format(b))
    if b == 2:
        break
    b += 1
else:
    print("this sentence should not be printed")