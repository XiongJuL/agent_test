import asyncio

async def process_webhook_event(payload):
    print("收到 Webhook 事件，开始处理...")

    # 错误 1：键名拼写错误 (KeyError)
    # 假设 payload 里其实叫 "event_type"，你写成了 "event"
    event_name = payload["event"] 
    print(f"事件类型: {event_name}")

    # 错误 2：类型拼接错误 (TypeError)
    # user_id 通常是整数 (int)，不能直接跟字符串用 + 拼接
    user_id = payload["user_id"]
    welcome_msg = "欢迎用户: " + user_id 
    print(welcome_msg)

    # 错误 3：异步调用错误 (TypeError)
    # 假设 save_to_db 是一个异步函数 (async def)，但这里忘了加 await
    save_to_db(payload) 

    # 错误 4：变量名未定义 (NameError)
    # 把 payload 拼写错了
    if paylaod.get("is_critical"):
        print("⚠️ 这是一个严重警报！")

    # 错误 5：除零错误 (ZeroDivisionError)
    # 如果 items 是空列表，len(items) 就是 0
    items = payload.get("items", [])
    total = sum(items)
    average = total / len(items) 
    print(f"平均值: {average}")

    # 错误 6：空对象属性错误 (AttributeError)
    # 假设数据库连接没建好，是个 None
    db_connection = None 
    db_connection.commit() # 对 None 调用 .commit() 会崩溃

    return True


async def save_to_db(data):
    await asyncio.sleep(0.1)
    print("数据已保存到数据库")


# --- 测试数据 ---
test_payload = {
    "event_type": "push",
    "user_id": 10086,
    "items": [],
    "is_critical": False
}

# 运行异步主函数
asyncio.run(process_webhook_event(test_payload))
