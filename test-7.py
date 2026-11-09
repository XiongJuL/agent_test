import sqlite3
import time
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_PASSWORD = os.environ.get("DB_PASSWORD")
SECRET_KEY = os.environ.get("SECRET_KEY")

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
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

def process_payment(user_id, amount):
    print(f"Processing payment for user {user_id}...")
    try:
        time.sleep(1)
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "payment_log.txt")
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
    username = "XiongJiuL"
    scores = [85, 90, 78]

    print(f"Fetching data for {username}")
    user_data = get_user_data(username)

    print("Calculating average...")
    avg = calculate_average(scores)

    print(f"Average is: {avg}")

    process_payment(1001, -50)

if __name__ == "__main__":
    main()