import math_util
from persistence import log_api_call


def pow(base: float, exponent: float) -> float:
    result = math_util.pow(base, exponent)
    log_api_call("pow", f"base={base}, exponent={exponent}", str(result))
    return result


def factorial(n: int) -> int:
    result = math_util.factorial(n)
    log_api_call("factorial", f"n={n}", str(result))
    return result


def fibonacci(n: int) -> int:
    result = math_util.fibonacci(n)
    log_api_call("fibonacci", f"n={n}", str(result))
    return result
