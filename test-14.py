import asyncio

async def process_webhook_event(payload):
    print("收到 Webhook 事件，开始处理...")

    # 1. 修复 KeyError：使用 .get() 安全获取
    event_name = payload.get("event_type")
    print(f"事件类型: {event_name}")

    # 2. 修复重复赋值：只保留一次
    user_id = payload.get("user_id")
    welcome_msg = f"欢迎用户： {user_id}"
    print(welcome_msg)

    # 3. 修复语法/缩进错误：正确判断数据库连接
    db_connection = None  # 模拟数据库连接
    if db_connection is not None:
        db_connection.commit()
    else:
        raise RuntimeError("数据库连接不可用，无法提交事务")

    # 4. 修复除以零错误 & 变量未定义
    items = payload.get("items", [])
    if items:
        total = sum(items)
        average = total / len(items)
        print(f"平均值: {average}")
    else:
        print("items 为空，无法计算平均值")

    # 5. 修复未定义的异步函数
    await save_to_db(payload)
    print("数据已成功保存到数据库")


async def save_to_db(data):
    await asyncio.sleep(0.1)  # 模拟耗时
    print("数据已保存到数据库")


# --- 测试数据 ---
test_payload = {
    "event_type": "push",
    "user_id": 10086,
    "items": [10, 20, 30],
    "is_critical": False
}

# 运行测试
# asyncio.run(process_webhook_event(test_payload))
