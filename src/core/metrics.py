from prometheus_client import Counter, Histogram

EXTERNAL_API_CALLS_TOTAL = Counter(
    'app_external_api_calls_total',  
    'Total number of calls made to the external API.',
    ['status']
)

EXTERNAL_API_CALL_DURATION_SECONDS = Histogram(
    'app_external_api_call_duration_seconds',
    'Histogram of external API call duration in seconds.',
    ['status']
)