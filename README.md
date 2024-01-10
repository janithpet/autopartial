# Autopartial

This is a simple library that provides a decorator that allows your to apply a function partially. In other words, it allows you to curry a function with some of its arguments, from left to right.

## Installation
After cloning this repository, you can install the package by running the following command in the root directory of the repository:
```bash
pip install -e .
```

## Usage and example
The main use case is to decorate a function definition with `@autopartial`.

An example can is in `main.py`. It contains the following code:
```python
from autopartial import autopartial

@autopartial
def add(x, y):
	return x + y

if __name__ == '__main__':
	x = 10
	y = 20

	add_10 = add(x)	# add(x): y -> x + y
	print(add_10(y)) # 30
```

Here, the `add` function takes 2 arguments and returns its sum. You can now partially apply the argument `x` to `add` by calling `add(x)`. This returns a new function that takes only one argument `y` and returns  `x + y`.

In the example above, `add(10)` returns a function `add_10` that always adds 10 to its input.

You can run this example, after installing this package, by running the following command from the root of the repository:
```bash
python main.py
```
