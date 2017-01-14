def is_even(x):
    return (x % 2) == 0


def is_odd(x):
    return (x % 2) != 0


def provider(func, x):
    return func(x)

for i in range(10):
    print(f"Is {i} odd? ", provider(is_odd, i))
    print(f"Is {i} even? ", provider(is_even, i))
