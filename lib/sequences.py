#!/usr/bin/env python3

def print_fibonacci(length):
    """
    Prints a list containing the Fibonacci sequence up to the specified length.

    Args:
        length (int): The number of Fibonacci numbers to generate.
    """
    if length <= 0:
        print([])
        return

    fib_sequence = [0]
    if length == 1:
        print(fib_sequence)
        return

    fib_sequence.append(1)

    while len(fib_sequence) < length:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)

    print(fib_sequence)

if __name__ == "__main__":
    print_fibonacci(9)
