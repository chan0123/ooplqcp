class RangeIterator:

	# constructor
	def __init__(self, first, last):
		self.last = last
		self.current_position = first

	# make it iteratable	
	def __iter__(self):
		return self

	# make it comply to next 
	# for python 2.X, use next() instead of __next__()
	def next(self):
		if self.current_position == self.last:
			raise StopIteration

		original_position = self.current_position	
		# increment to get the next position
		self.current_position = self.current_position + 1
		return original_position