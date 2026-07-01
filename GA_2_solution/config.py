# ==========================================
# MASTER CONFIGURATION CHEAT SHEET
# Filled in with 24f2006167 assigned values
# ==========================================

# 1. Your IITM Email
EMAIL = "24f2006167@ds.study.iitm.ac.in"

# 2. Q1: CORS Allowed Origin
Q1_ALLOWED_ORIGIN = "https://dash-gcu3wn.example.com"

# 3. Q2: OAuth JWKS (Issuer, Audience, and Public Key)
ISSUER = "https://idp.exam.local"
AUDIENCE = "tds-q7lth2tf.apps.exam.local"
PUBLIC_KEY_PEM = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2okOHspNjgA+2rTLbeuY
cxiP/hG8C6Sb9iwg3yiLAA4HCnpITcbWCSelbvbYGuc3EbNy4xFyf5Cbj5DHJMID
EkryOgyd2giIIIBOUBj8S63uGcnRpOBh9NFatfNwheKuzsPuVNldu6A9cNteNpXc
WyJjG2axVfmq7i6SuKr1JoWYG7xTTAvKPujSl40tsQf03h5NepzdfXpr28oNnzfW
ed+zclR6BcmNNo/WVfJ4xyCLSf0BCOgdTgW6PdaChd1l9VDetJZVEgC5tkyvXsfI
SI6iyrYbKR0NEBSqq4XkadEjsCs4F1RncsS4LlgniT7GlkL9Mce3b0wGLs9/7ZIX
dQIDAQAB
-----END PUBLIC KEY-----"""

# 4. Q3: 12-Factor Config
# Precedence:
# OS Env (APP_*) > .env file > YAML > Defaults
#
# Resolved values:
# APP_PORT = 8101      (OS env)
# APP_WORKERS = 2      (OS env)
# APP_DEBUG = false    (OS env)
# log_level = warning  (YAML)
#
Q3_PORT = 8101
Q3_WORKERS = 2
Q3_DEBUG = False
Q3_LOG_LEVEL = "warning"

# 5. Q5: Analytics API key
Q5_API_KEY = "ak_rzubew751cnw5mplohprvhxo"

# 6. Q9: Idempotency & Pagination & Rate Limit
Q9_TOTAL_ORDERS = 42
Q9_RATE_LIMIT = 18

# 7. Q10: Middleware Rate Limit
Q10_ALLOWED_ORIGIN = "https://app-1n5lzz.example.com"
Q10_RATE_LIMIT = 13

# ==========================================
# FIXED VARIABLES (Do not change these)
# ==========================================

EXAM_PORTAL_ORIGIN = "https://exam.sanand.workers.dev"