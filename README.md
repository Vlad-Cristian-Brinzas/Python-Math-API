# Python Math API

A Python-based API for mathematical operations, built for the DavaX programme. This project demonstrates a FastAPI application with Kafka-based logging, database persistence, and Prometheus monitoring. The system is fully containerized and orchestrated via Docker Compose.

## Features
- **Power Function**: Calculate `base` raised to the power of `exponent`.
- **Factorial Function**: Compute the factorial of a non-negative integer.
- **Fibonacci Function**: Get the nth Fibonacci number.
- **API Call Logging**: All operations are logged to a Kafka topic and persisted to a local SQLite database by a dedicated log consumer service.
- **Prometheus Monitoring**: Exposes metrics for API usage on a separate port.
- **Kafka Integration**: Decoupled logging using Kafka and a separate consumer service.
- **Dockerized**: All services (API, log consumer, Kafka, Prometheus) are managed via Docker Compose for easy deployment and development.

## Requirements
- Docker & Docker Compose (recommended for all usage due to Kafka dependency)

## Installation & Usage

### Recommended: With Docker Compose
1. Build and start all services:
   ```bash
   docker-compose up --build
   ```
2. The API will be available at [http://localhost:8000](http://localhost:8000)
3. Prometheus metrics at [http://localhost:8001](http://localhost:8001)
4. Prometheus UI at [http://localhost:9090](http://localhost:9090)

> **Note:** Due to the Kafka dependency, running the API outside Docker Compose is not recommended. All services (API, Kafka, log consumer, Prometheus) are orchestrated together for a seamless experience.

## API Endpoints
- `GET /pow?base=<float>&exponent=<float>`: Power function
- `GET /factorial?n=<int>`: Factorial function
- `GET /fibonacci?n=<int>`: Fibonacci function

## Project Structure
```
┌─ app/
│  ├─ main.py                    FastAPI app entry point
│  ├─ controllers/               API route definitions
│  ├─ services/                  Business logic and Kafka producer
│  ├─ utils/                     Math utility functions
│  └─ monitoring/                Prometheus metrics server setup
├─ log_consumer/
│  ├─ log_consumer.py            Kafka consumer and DB logger
│  ├─ persistence.py             SQLite persistence logic
│  ├─ requirements.txt           Dependencies for the consumer service
│  └─ Dockerfile                 Dockerfile for the log consumer
├─ shared/                       Shared Pydantic models
├─ data/                         SQLite database and Kafka data (persisted by Docker)
├─ requirements.txt              Python dependencies for the API
├─ docker-compose.yml            Containerization setup
├─ docker-compose.override.yml   Overrides for development ease-of-use
├─ Dockerfile                    Dockerfile for the API
└─ prometheus.yml                Prometheus configuration
```

## Extending
You can add new mathematical operations by updating `app/utils/` and `app/services/`, and exposing new endpoints in `app/controllers/` and `app/main.py`. Logging and monitoring will be handled automatically if you follow the existing patterns.

---

*Created for the DavaX programme. For educational/demo purposes.*
