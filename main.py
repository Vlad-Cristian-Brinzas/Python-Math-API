from fastapi import FastAPI, HTTPException, Query
from persistence import setup_database
from monitoring import prometheus_counter
from services import pow, factorial, fibonacci

setup_database()  # Ensure the database is set up before starting the API
app = FastAPI(
    title="Math Utility API",
    description=(
        "Small API for mathematical operations "
        "like power, factorial, and Fibonacci sequence."
    )
)
# About "mandatory to use Pydantic for request validation":
# FastAPI uses Pydantic internally anyway, so we technically meet that?
# Similar for "any non-SOAP API standard":
# FastAPI is HTTP-based by default.


@app.get(
    "/pow",
    summary="Power Function",
    description="Raises a number to the power of an exponent."
)
def compute_power(base: float = Query(...), exponent: float = Query(...)):
    prometheus_counter.labels(method="GET", endpoint="/pow").inc()
    return {"result": pow(base, exponent)}


@app.get(
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


@app.get(
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
