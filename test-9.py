import time
import re
import hashlib
import asyncio

# ==========================================
# 雷区 1：面向对象陷阱（类变量误用与内存泄漏）
# ==========================================
class UserSessionManager:
    # 致命错误：可变对象作为类变量。所有实例共享这一个列表！
    active_sessions = [] 

    def __init__(self, user_id):
        self.user_id = user_id
        # 错误：试图在初始化时往共享列表里加数据
        self.active_sessions.append(user_id) 

    def destroy_session(self):
        # 错误：这会导致越删越乱，因为大家操作的是同一个列表
        self.active_sessions.remove(self.user_id)


# ==========================================
# 雷区 2：Web 后端终极灾难（在 async 中使用阻塞调用）
# ==========================================
async def fetch_user_data_from_third_party(user_id):
    print("Fetching data...")
    # 致命错误：在 async 异步函数中使用了 time.sleep（同步阻塞）
    # 这会导致整个 FastAPI 的 Event Loop 卡死，服务器直接假死！
    time.sleep(5) 
    
    # 错误：没有处理 requests 的异常和超时
    # response = requests.get(f"https://api.example.com/{user_id}")
    return {"id": user_id, "status": "ok"}


# ==========================================
# 雷区 3：安全灾难（正则表达式 ReDoS 漏洞 & 弱哈希）
# ==========================================
def validate_email_and_hash(email):
    # 危险：极度复杂的正则，容易引发 ReDoS（灾难性回溯）攻击
    # 攻击者只需发送一个极长的恶意字符串，就能让服务器 CPU 100%
    email_pattern = r"^([a-zA-Z0-9])(([\-.]|[_]+)?([a-zA-Z0-9]+))*(@){1}[a-z0-9]+[\.]{1}([a-z]{2,3})$"
    if not re.match(email_pattern, email):
        raise ValueError("Invalid email")
    
    # 错误：使用已被破解的 MD5 对密码/敏感信息进行哈希
    # 并且没有加盐（Salt），极易被彩虹表撞库
    hashed_pwd = hashlib.md5(email.encode()).hexdigest()
    return hashed_pwd


# ==========================================
# 雷区 4：危险的动态执行与逻辑黑洞
# ==========================================
def calculate_formula(formula_str):
    # 致命安全漏洞：直接使用 eval 执行用户输入的字符串
    # 如果用户输入 "__import__('os').system('rm -rf /')"，你的服务器就没了
    try:
        result = eval(formula_str)
        return result
    except:
        # 错误：盲目捕获所有异常，并且什么都不做
        # 如果这里出错了，返回的是 None，调用方如果不做判断，后续直接连环崩溃
        pass 


# ==========================================
# 雷区 5：异常处理的反面教材
# ==========================================
def process_order(order_id):
    try:
        # 假设这里有一段复杂的业务逻辑
        pass
    except Exception as e:
        # 错误：抛出了一个字符串而不是异常对象，且丢失了原始的 traceback
        raise "Order processing failed" 
