from functools import lru_cache


# With floating-point inputs, LRU cache may not be very worth it.
def pow(base: float, exponent: float) -> float:
    """
    Raises a number to the power of an exponent.

    :param number: The base number.
    :param exponent: The exponent to raise the base number to.
    :return: The result of raising the base number to the exponent.
    """
    return base ** exponent
    # TODO: not sure just using the inbuilt ** is a permissible approach


@lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    """
    Computes the nth Fibonacci number.

    :param n: The position in the Fibonacci sequence (0-indexed).
    :return: The nth Fibonacci number.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
        # Recursive approach for memoization effciency


@lru_cache(maxsize=128)
def factorial(n: int) -> int:
    """
    Computes the factorial of a non-negative integer n.

    :param n: A non-negative integer.
    :return: The factorial of n.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
        # Recursive approach for memoization efficiency
