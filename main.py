from autopartial import autopartial

@autopartial
def f(x, y):
	return x + y

if __name__ == '__main__':
	x = 10
	y = 20

	g = f(x)	# f(x): y -> x + y
	print(g(y)) # 30

