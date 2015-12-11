#!/usr/bin/env python3

#def my_map(function, iterateable):
#	assert     hasattr(iterateable, "__iter__")
#	return (function(item) for item in iterateable)

def my_map(function, iterateable_container):
	assert     hasattr(iterateable_container, "__iter__")
	for item in iterateable_container:
		yield function(item)