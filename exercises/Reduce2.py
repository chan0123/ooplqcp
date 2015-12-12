#!/usr/bin/env python3

# ----------
# Reduce2.py
# ----------

# https://docs.python.org/3.4/library/functools.html

def reduce_while (bf, a, v = None) :
    if (not a) and (v is None) :
        raise TypeError("reduce() of empty sequence with no initial value")
    if not a :
        return v
    p = iter(a)
    if v is None :
        v = next(p)
    try :
        while True :
            v = bf(v, next(p))
    except StopIteration :
        pass
    return v

def reduce_for (bf, a, v = None) :
    if (not a) and (v is None) :
        raise TypeError("reduce() of empty sequence with no initial value")
    if not a :
        return v
    p = iter(a)
    if v is None :
        v = next(p)
    for w in p :
        v = bf(v, w)
    return v
