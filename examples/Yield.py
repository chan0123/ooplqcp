#!/usr/bin/env python

# --------
# Yield.py
# --------

print "Yield.py"

def f () :
    yield 2
    yield 3
    yield 4

p = f() # wont call the function at all, will get a generator (which is a iterator)
n = next(p)
assert n == 2
n = next(p)
assert n == 3
n = next(p)
assert n == 4
try :
    n = next(p)
except StopIteration :
    pass

# this is how range works
def g () :
    for v in [2, 3, 4] :
        yield v

p = g()
n = next(p)
assert n == 2
n = next(p)
assert n == 3
n = next(p)
assert n == 4
try :
    n = next(p)
except StopIteration :
    pass

print "Done."
