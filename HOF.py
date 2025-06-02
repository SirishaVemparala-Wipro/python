def apply_twice(func, x):
    return func(func(x))

def square(x):
    return x * x

print(apply_twice(square, 2))  # Output: square(square(2)) = 16
