from prometheus_client import Counter, Histogram

HTTP_CLIENT_EXTERNAL_API_REQUESTS_TOTAL = Counter(
    'http_client_external_api_requests_total',
    'Total number of HTTP client requests made to the external API.',
    ['status']
)


HTTP_CLIENT_EXTERNAL_API_REQUEST_DURATION_SECONDS = Histogram(
    'http_client_external_api_request_duration_seconds',
    'Histogram of external API request duration in seconds.',
    ['status']
)