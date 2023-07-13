#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        toto = add(a, b)
        for i in range(4, 6):
            toto = add(toto, i)
        return toto
    else:
        return sub(a, b)
