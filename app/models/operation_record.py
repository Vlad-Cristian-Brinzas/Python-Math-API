from pydantic import BaseModel


class OperationRecord(BaseModel):
    """
    Data model for logging API calls.

    Attributes:
        operation (str): The mathematical operation performed.
        input_data (str): The input data used for the operation.
        result (str): The result of the operation.
    """
    operation: str
    input_data: str
    result: str
