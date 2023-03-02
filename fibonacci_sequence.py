# A number is the sum of its preceeding 2 numbers


def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        print(x,)
        yield x


# Output the first 15 fibonacci numbers
fibonacci(15)
