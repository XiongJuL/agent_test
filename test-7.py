import sqlite3
import time

# 雷区 1：硬编码敏感信息（安全隐患）
DB_PASSWORD = "admin123456"
SECRET_KEY = "super_secret_key"

def get_user_data(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # 雷区 2：经典 SQL 注入漏洞（不要直接拼接 SQL）
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    result = cursor.fetchall()
    
    # 雷区 3：资源泄漏（打开数据库连接后没有 close()）
    return result

def calculate_average(scores):
    # 雷区 4：除以零的风险（如果传入空列表）
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

def process_payment(user_id, amount):
    print(f"Processing payment for user {user_id}...")
    
    # 雷区 5：极其宽泛的异常捕获，掩盖了真实错误（代码异味）
    try:
        # 模拟一个耗时操作，可能会崩溃
        time.sleep(1)
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        
        # 雷区 6：硬编码本地路径和文件操作未关闭
        f = open("C:\\logs\\payment_log.txt", "a")
        f.write(f"User {user_id} paid {amount}\n")
        
    except Exception:
        pass # 吞掉异常，出事了连日志都不打，排查问题全靠猜

def main():
    # 雷区 7：极差的变量命名（a, b, c），毫无可读性
    a = "XiongJiuL"
    b = [85, 90, 78]
    
    # 触发漏洞点
    print(f"Fetching data for {a}")
    user_data = get_user_data(a)
    
    print("Calculating average...")
    avg = calculate_average(b)
    
    print(f"Average is: {avg}")
    
    # 触发异常点（负数金额）
    process_payment(1001, -50)

if __name__ == "__main__":
    main()
