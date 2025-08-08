from fastapi import APIRouter, HTTPException, Query
from services.math_service import pow, factorial, fibonacci
from monitoring import prometheus_counter


print("Setting up routes...")
math_router = APIRouter()


@math_router.get(
    "/pow",
    summary="Power Function",
    description="Raises a number to the power of an exponent."
)
def compute_power(base: float = Query(...), exponent: float = Query(...)):
    prometheus_counter.labels(method="GET", endpoint="/pow").inc()
    return {"result": pow(base, exponent)}


@math_router.get(
    "/factorial",
    summary="Factorial Function",
    description="Computes the factorial of a non-negative integer."
)
def compute_factorial(n: int = Query(..., ge=0)):
    prometheus_counter.labels(method="GET", endpoint="/factorial").inc()
    try:
        return {"result": factorial(n)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@math_router.get(
    "/fibonacci",
    summary="Fibonacci Function",
    description="Computes the nth Fibonacci number."
)
def compute_fibonacci(n: int = Query(..., ge=0)):
    prometheus_counter.labels(method="GET", endpoint="/fibonacci").inc()
    try:
        return {"result": fibonacci(n)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
