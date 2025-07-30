# Python Math API

A simple Python-based API for mathematical operations, built for the DavaX programme. This project demonstrates a FastAPI application with database persistence and Prometheus monitoring, and is easily extensible for further features.

## Features
- **Power Function**: Calculate `base` raised to the power of `exponent`.
- **Factorial Function**: Compute the factorial of a non-negative integer.
- **Fibonacci Function**: Get the nth Fibonacci number.
- **API Call Logging**: All operations are logged to a local SQLite database.
- **Prometheus Monitoring**: Exposes metrics for API usage on a separate port.
- **Dockerized**: Includes Docker and Docker Compose setup for easy deployment.

## Requirements
- Python 3.8+
- Docker & Docker Compose (for containerized usage)

## Installation & Usage

### 1. Local Development
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the API:
   ```bash
   uvicorn main:app --reload
   ```
3. Access the API docs at [http://localhost:8000/docs](http://localhost:8000/docs)

### 2. With Docker Compose
1. Build and start all services:
   ```bash
   docker-compose up --build
   ```
2. The API will be available at [http://localhost:8000](http://localhost:8000)
3. Prometheus metrics at [http://localhost:8001](http://localhost:8001)
4. Prometheus UI at [http://localhost:9090](http://localhost:9090)

## API Endpoints
- `GET /pow?base=<float>&exponent=<float>`: Power function
- `GET /factorial?n=<int>`: Factorial function
- `GET /fibonacci?n=<int>`: Fibonacci function

## Project Structure
- `main.py` — FastAPI app entry point
- `services.py` — Business logic for math operations
- `persistence.py` — SQLite database setup and logging
- `monitoring.py` — Prometheus metrics server
- `math_util.py` — Math utility functions (implementations)
- `requirements.txt` — Python dependencies
- `docker-compose.yml`, `Dockerfile` — Containerization setup

## Extending
You can add new mathematical operations by updating `math_util.py` and `services.py`, and exposing new endpoints in `main.py`.

---

*Created for the DavaX programme. For educational/demo purposes.*
