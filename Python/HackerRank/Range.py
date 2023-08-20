# The `range()` function in Python is used to generate a sequence of numbers. It can be used in various ways to create a range of integers for iteration or other purposes. The `range()` function has three forms:

# 1. `range(stop)`: Generates a sequence of numbers from 0 to `stop - 1`.
# 2. `range(start, stop)`: Generates a sequence of numbers from `start` to `stop - 1`.
# 3. `range(start, stop, step)`: Generates a sequence of numbers from `start` to `stop - 1`, incrementing by `step` each time.

# Here are some examples to illustrate how the `range()` function works:

# Example 1: Generating a sequence from 0 to stop - 1
for i in range(5):
    print(i)  # Output: 0 1 2 3 4 (Printed in new line)

# Example 2: Generating a sequence from start to stop - 1
for i in range(2, 7):
    print(i)  # Output: 2 3 4 5 6 (Printed in new line)

# Example 3: Generating a sequence with a custom step
for i in range(1, 10, 2):
    print(i)  # Output: 1 3 5 7 9 (Printed in new line)

# The `range()` function is commonly used in loops, such as `for` loops, to iterate over a sequence of numbers. It's important to note that the `stop` value is not included in the generated sequence, so if you want to include it, you'll need to use `stop + 1` as the endpoint or adjust your logic accordingly.
# For printing in same line:
for i in range(5):
    print(i, end = ' ')  # Output: 0 1 2 3 4
