import os

JWT_SECRET = os.environ.get("JWT_SECRET", "changeme")
# RDS_URI = os.environ.get("RDS_URI", "changeme")
RDS_URI = 'postgres+psycopg2://Nathan:@localhost:5432/backend'
IS_PRODUCTION = os.environ.get("IS_PRODUCTION", False)

#common service code pairs
OIL_CHANGE_CODE_PAIR = ('Oil change', 'OC1')
COMMON_SERVICE_PAIRS = [OIL_CHANGE_CODE_PAIR]

#common service codes
OIL_CHANGE_CODE = 'OC1'
COMMON_SERVICE_CODES = [OIL_CHANGE_CODE]