import os
import sqlite3
import random

# ==========================================
# 雷区 1：语法错误 (Syntax Error)
# 缺少右括号和冒号，代码根本无法运行，IDE 会直接标红
# ==========================================
def initialize_system(env
    print("System initializing...") 
    

# ==========================================
# 雷区 2：逻辑错误 & 变量作用域 (Logical Error)
# 代码能跑，但结果永远不对
# ==========================================
def calculate_discount(price, discount_rate):
    # 错误：这里用了赋值符 = 而不是比较符 ==
    if discount_rate = 0.5:
        return price * 0.5
    
    # 错误：局部变量在循环外使用（如果循环没执行会报 NameError）
    for i in range(0):
        total = price
    return total * discount_rate


# ==========================================
# 雷区 3：致命的安全漏洞与资源泄漏 (Security & Leaks)
# ==========================================
def get_user_profile(username):
    # 漏洞 1：硬编码数据库密码
    password = "admin123"
    
    # 漏洞 2：资源未释放（没有 close）
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    
    # 漏洞 3：经典 SQL 注入（直接使用字符串格式化）
    query = f"SELECT * FROM users WHERE name = '{username}'"
    cursor.execute(query)
    
    # 漏洞 4：极其宽泛的异常捕获，吞掉了所有错误
    try:
        result = cursor.fetchone()
    except Exception:
        pass
    
    return result


# ==========================================
# 雷区 4：运行时致命崩溃 (Runtime Error)
# ==========================================
def process_scores(scores):
    # 错误 1：列表越界（取第 1 个元素，但列表只有 1 个元素）
    first_score = scores[1] 
    
    # 错误 2：除以零 (ZeroDivisionError)
    # 因为列表长度可能是 0，直接做除法必崩
    average = sum(scores) / 0 
    
    # 错误 3：类型不匹配 (TypeError)
    message = "The average is: " + average 
    
    return message


# ==========================================
# 雷区 5：经典的 Python 可变默认参数陷阱
# ==========================================
def add_log(log_message, log_list=[]):
    log_list.append(log_message)
    return log_list


if __name__ == "__main__":
    # 触发各种崩溃
    user = get_user_profile("admin' OR '1'='1") # 触发 SQL 注入
    
    scores = []
    print(process_scores(scores)) # 直接触发 IndexError
    
    # 测试默认参数陷阱
    print(add_log("Error 1"))
    print(add_log("Error 2")) # 你会发现输出里包含了 "Error 1"，这就是 Bug
