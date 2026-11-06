import asyncio

async def process_webhook_event(payload):
    print("收到 Webhook 事件，开始处理...")

    event_name = payload.get("event_type")
    if event_name is None:
        print("缺少 event_type，无法处理事件")
        return False
    print(f"事件类型: {event_name}")

    user_id = payload.get("user_id")
    if user_id is None:
        print("缺少 user_id，无法处理事件")
        return False
    welcome_msg = f"欢迎用户: {user_id}"
    print(welcome_msg)

    await save_to_db(payload)

    if payload.get("is_critical"):
        print("⚠️ 这是一个严重警报！")

    items = payload.get("items", [])
    numeric_items = [item for item in items if isinstance(item, (int, float)) and not isinstance(item, bool)]
    if len(numeric_items) != len(items):
        print("items 中包含非数值元素，已忽略非数值项")
    total = sum(numeric_items)
    if len(numeric_items) > 0:
        average = total / len(numeric_items)
        print(f"平均值: {average}")
    else:
        print("平均值: 无法计算（items 为空或无数值项）")

    db_connection = await get_db_connection()
    if db_connection is not None:
        db_connection.commit()
    else:
        print("数据库连接无效，跳过提交")

    return True


async def get_db_connection():
    await asyncio.sleep(0.05)
    return _FakeConnection()


class _FakeConnection:
    def commit(self):
        print("数据库事务已提交")


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
