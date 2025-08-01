import utils.math_util as math_util
from models import OperationRecord
from services.persistence import log_api_call


def pow(base: float, exponent: float) -> float:
    result = math_util.pow(base, exponent)
    log_api_call(OperationRecord(
        operation="pow",
        input_data=f"base={base}, exponent={exponent}",
        result=str(result))
    )
    return result


def factorial(n: int) -> int:
    result = math_util.factorial(n)
    log_api_call(OperationRecord(
        operation="factorial",
        input_data=f"n={n}",
        result=str(result))
    )
    return result


def fibonacci(n: int) -> int:
    result = math_util.fibonacci(n)
    log_api_call(OperationRecord(
        operation="fibonacci",
        input_data=f"n={n}",
        result=str(result))
    )
    return result
