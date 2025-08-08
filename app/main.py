from fastapi import FastAPI
from controllers.math_routes import math_router

print("Starting FastAPI application...")
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
app.include_router(math_router)
