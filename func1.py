def is_even(x):
    return (x % 2) == 0

print(list(filter(is_even, range(10))))
