import time
import re
import hashlib
import asyncio
import logging
import secrets
import hmac

logger = logging.getLogger(__name__)


class UserSessionManager:
    def __init__(self, user_id):
        self.user_id = user_id
        self.active_sessions = []

    def add_session(self):
        self.active_sessions.append(self.user_id)

    def destroy_session(self):
        if self.user_id in self.active_sessions:
            self.active_sessions.remove(self.user_id)


async def fetch_user_data_from_third_party(user_id):
    logger.info("Fetching data for user %s", user_id)
    await asyncio.sleep(5)
    return {"id": user_id, "status": "ok"}


EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


def validate_email_and_hash(email):
    if not isinstance(email, str) or len(email) > 254:
        raise ValueError("Invalid email")
    if not EMAIL_PATTERN.match(email):
        raise ValueError("Invalid email")

    salt = secrets.token_bytes(16)
    dk = hashlib.pbkdf2_hmac("sha256", email.encode(), salt, 100000)
    return salt.hex() + ":" + dk.hex()


ALLOWED_CHARS = set("0123456789+-*/(). ")


def calculate_formula(formula_str):
    if not isinstance(formula_str, str):
        raise ValueError("Formula must be a string")
    if not formula_str or len(formula_str) > 200:
        raise ValueError("Invalid formula length")
    if not set(formula_str).issubset(ALLOWED_CHARS):
        raise ValueError("Invalid characters in formula")
    try:
        result = eval(formula_str, {"__builtins__": {}}, {})
        return result
    except Exception as e:
        logger.exception("Failed to evaluate formula")
        raise ValueError("Invalid formula") from e


def process_order(order_id):
    try:
        pass
    except Exception as e:
        logger.exception("Order processing failed for order %s", order_id)
        raise RuntimeError("Order processing failed") from e
