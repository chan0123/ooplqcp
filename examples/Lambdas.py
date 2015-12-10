#!/usr/bin/env python3

# ----------
# Lambdas.py
# ----------

def add_function (i, j) :
    return i + j

def add_lambda () :
    return lambda i, j : i + j

def add_closure_1 (i) :
    return lambda j : i + j

def add_closure_2 (x) :
    return lambda j : x[0] + j

def add_closure_3 (x) :
    def f (y) :
        v     = x[0]
        x[0] += 1
        return v + y
    return f

print("Lambdas.py")

assert add_function(2, 3) == 5
f = add_function
assert f(2, 3) == 5

assert add_lambda()(2, 3) == 5
f = add_lambda()
assert f(2, 3) == 5

i = 2
f = add_closure_1(i)
assert f(3) == 5
assert i    == 2

x = [2]
f = add_closure_2(x)
x = [3]
assert f(3) == 5
assert x == [3]

x = [1]
f = add_closure_2(x)
x[0] = 2
assert f(3) == 5
assert x == [2]

x = [2]
f = add_closure_3(x)
assert f(3) == 5
assert x == [3]

print("Done.")
