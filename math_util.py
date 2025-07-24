def pow(number: float, exponent: float) -> float:
    """
    Raises a number to the power of an exponent.

    :param number: The base number.
    :param exponent: The exponent to raise the base number to.
    :return: The result of raising the base number to the exponent.
    """
    return number ** exponent
    # TODO: not sure just using the inbuilt ** is a permissible approach


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
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    # TODO: this is not a very efficient implementation as n grows large


def factorial(n: int) -> int:
    """
    Computes the factorial of a non-negative integer n.

    :param n: A non-negative integer.
    :return: The factorial of n.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
