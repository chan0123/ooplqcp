#!/usr/bin/env python3

def my_reduce(binary_function, list, seed):
	assert type(seed) is int
	for number in list:
		seed = binary_function(seed, number)	
	return seed