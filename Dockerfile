# Use a slim Python image
FROM python:3.13.5-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY ./ ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the app runs on
EXPOSE 8000

# Start the FastAPI application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
