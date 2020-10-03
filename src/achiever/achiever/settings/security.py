# SECURITY WARNING: keep the secret key used in production secret!
# Korobov TODO: Move this to .env and use dotenv
SECRET_KEY = '(n(hhdldw0cadn=5l2w8ahf2aq3gpa3)aezxq1d^m%w*pic_ef'

# CORS integration
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'enctype',
    'x-device_id',
    'x-device_type',
    'x-auth-token'
]

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = (
    '127.0.0.1:8080',
    '127.0.0.1:8888',
    '127.0.0.1',
)