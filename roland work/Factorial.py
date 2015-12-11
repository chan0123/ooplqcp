#!/usr/bin/env python3

def my_factorial(n):
	assert n >= 0
	result = 1
	if (n==0):
		return 1
	for i in range(2, n+1):
		result = result * i
	return result