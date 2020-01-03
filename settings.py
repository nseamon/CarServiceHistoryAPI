import os

JWT_SECRET = os.environ.get("JWT_SECRET", "changeme")
RDS_URI = os.environ.get("RDS_URI", "changeme")
IS_PRODUCTION = os.environ.get("IS_PRODUCTION", False)