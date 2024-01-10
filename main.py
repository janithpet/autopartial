from autopartial import autopartial

@autopartial
def add(x, y):
	return x + y

if __name__ == '__main__':
	x = 10
	y = 20

	add_10 = add(x)	 # add(x): y -> x + y
	print(add_10(y)) # 30

