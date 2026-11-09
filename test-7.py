import sqlite3
import time
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_PASSWORD = os.environ.get("DB_PASSWORD")
SECRET_KEY = os.environ.get("SECRET_KEY")

PAYMENT_LOG_FILENAME = "payment_log.txt"
MIN_PAYMENT_AMOUNT = 0
PAYMENT_SIMULATED_DELAY_SECONDS = 1
DEFAULT_USERNAME = "XiongJiuL"
DEFAULT_SCORES = [85, 90, 78]
DEFAULT_PAYMENT_USER_ID = 1001
DEFAULT_PAYMENT_AMOUNT = 50

def get_user_data(username):
    conn = sqlite3.connect("users.db")
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username = ?"
        cursor.execute(query, (username,))
        result = cursor.fetchall()
        return result
    finally:
        conn.close()

def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

def process_payment(user_id, amount):
    logger.info(f"Processing payment for user {user_id}...")
    try:
        time.sleep(PAYMENT_SIMULATED_DELAY_SECONDS)
        if amount < MIN_PAYMENT_AMOUNT:
            raise ValueError("Amount cannot be negative")
        log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), PAYMENT_LOG_FILENAME)
        with open(log_path, "a") as f:
            f.write(f"User {user_id} paid {amount}\n")
    except ValueError as e:
        logger.error(f"Invalid payment amount for user {user_id}: {e}")
        raise
    except OSError as e:
        logger.error(f"File operation failed for user {user_id}: {e}")
        raise
    except Exception as e:
        logger.exception(f"Unexpected error processing payment for user {user_id}: {e}")
        raise

def main():
    username = DEFAULT_USERNAME
    scores = DEFAULT_SCORES

    logger.info(f"Fetching data for {username}")
    user_data = get_user_data(username)

    logger.info("Calculating average...")
    avg = calculate_average(scores)

    logger.info(f"Average is: {avg}")

    try:
        process_payment(DEFAULT_PAYMENT_USER_ID, DEFAULT_PAYMENT_AMOUNT)
    except Exception as e:
        logger.error(f"Payment processing failed: {e}")

if __name__ == "__main__":
    main()
</final_file>