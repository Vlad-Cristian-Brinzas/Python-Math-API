import utils.math_util as math_util
from shared.models import OperationRecord
from services.kafka_messaging import send_operation_record


def pow(base: float, exponent: float) -> float:
    result = math_util.pow(base, exponent)
    send_operation_record(OperationRecord(
        operation="pow",
        input_data=f"base={base}, exponent={exponent}",
        result=str(result))
    )
    return result


def factorial(n: int) -> int:
    result = math_util.factorial(n)
    send_operation_record(OperationRecord(
        operation="factorial",
        input_data=f"n={n}",
        result=str(result))
    )
    return result


def fibonacci(n: int) -> int:
    result = math_util.fibonacci(n)
    send_operation_record(OperationRecord(
        operation="fibonacci",
        input_data=f"n={n}",
        result=str(result))
    )
    return result
