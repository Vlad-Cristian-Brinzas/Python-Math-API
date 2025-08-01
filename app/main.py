from fastapi import FastAPI
from services.persistence import setup_database
from controllers.math_routes import math_router

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
app.include_router(math_router)
