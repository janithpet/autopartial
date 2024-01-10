import inspect
from functools import partial

def autopartial(func):
	num_args = len(inspect.signature(func).parameters)
	def wrapper(*args):
		if len(args) > num_args:
			raise TypeError('Too many arguments')

		if len(args) == num_args:
			return func(*args)

		return autopartial(partial(func, *args))

	return wrapper