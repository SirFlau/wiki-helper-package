import os
import jwt
from datetime import datetime
from typing import Dict, Tuple, Optional


def authenticate_user(token: str) -> Tuple[bool, Optional[Dict]]:
    try:
        token_data = jwt.decode(token, os.environ["JWTSECRET"], algorithms="HS256")
    except jwt.exceptions.InvalidSignatureError:
        return False, {"message": "failed to decode jwt token"}
    if token_data["expiration"] < datetime.now().timestamp():
        return False, {"message": "jwt token expired"}
    return True, token_data
