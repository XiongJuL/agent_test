import asyncio

async def process_webhook_event(payload):
    print("收到 Webhook 事件，开始处理...")

    event_name = payload["event_type"]
    print(f"事件类型: {event_name}")

    user_id = payload["user_id"]
    welcome_msg = f"欢迎用户: {user_id}"
    print(welcome_msg)

    await save_to_db(payload)

    if payload.get("is_critical"):
        print("⚠️ 这是一个严重警报！")

    items = payload.get("items", [])
    total = sum(items)
    if len(items) > 0:
        average = total / len(items)
        print(f"平均值: {average}")
    else:
        print("平均值: 无法计算（items 为空）")

    db_connection = None
    if db_connection is not None:
        db_connection.commit()
    else:
        print("数据库连接无效，跳过提交")

    return True


async def save_to_db(data):
    await asyncio.sleep(0.1)
    print("数据已保存到数据库")


test_payload = {
    "event_type": "push",
    "user_id": 10086,
    "items": [],
    "is_critical": False
}

asyncio.run(process_webhook_event(test_payload))
