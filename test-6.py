# 欢迎来到 CodeGuard 专属靶场（纯正的烂代码）
import random

def process_user_data(user_info, scores=[]):
    # 雷区 1：经典的默认参数陷阱（可变对象），多次调用会累积数据
    scores.append(random.randint(1, 100))
    
    # 雷区 2：没有做 None 值判断，直接取值
    user_name = user_info["name"]
    
    # 雷区 3：用 + 号拼接字符串和数字（直接报 TypeError）
    welcome_msg = "Hello " + user_name + ", your score is " + scores[0]
    
    # 雷区 4：变量未定义就使用
    final_score = total_score * 2
    
    return welcome_msg, final_score

# 测试调用
if __name__ == "__main__":
    print("--- 程序开始 ---")
    
    # 这里传个缺少 "name" 键的字典进去
    data = {"id": 123, "age": 25}
    
    # 触发死局
    result = process_user_data(data)
    print(result)
