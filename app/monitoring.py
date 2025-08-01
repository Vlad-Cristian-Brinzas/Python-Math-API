from prometheus_client import start_http_server, Counter

prometheus_counter = Counter(
    'api_requests_total',
    'Total number of API requests',
    ['method', 'endpoint']
)

# Start the Prometheus metrics server
start_http_server(8001)  # Expose metrics on port 8001
