# Use a slim Python image
FROM python:3.13.5-slim

# Set working directory
WORKDIR /consumer

# Working relative to BUILD CONTEXT
# Therefore, write as if we're in root,
# not in /log_consumer

# Copy requirements file
COPY log_consumer/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY shared/ shared/
COPY log_consumer/ .

# Run Python
CMD ["python", "log_consumer.py"]
