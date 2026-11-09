import asyncio

EVENT_TYPE_KEY = "event_type"
USER_ID_KEY = "user_id"
ITEMS_KEY = "items"
IS_CRITICAL_KEY = "is_critical"


async def process_webhook_event(payload):
    """处理 Webhook 事件并保存到数据库。"""
    print("收到 Webhook 事件，开始处理...")

    event_name = payload.get(EVENT_TYPE_KEY)
    if event_name is None:
        print("缺少事件类型，无法处理")
        return False
    print(f"事件类型: {event_name}")

    user_id = payload.get(USER_ID_KEY)
    if user_id is None:
        print("缺少用户ID，无法处理")
        return False
    welcome_msg = f"欢迎用户: {user_id}"
    print(welcome_msg)

    await save_to_db(payload)

    if payload.get(IS_CRITICAL_KEY):
        print("⚠️ 这是一个严重警报！")

    items = payload.get(ITEMS_KEY, [])
    numeric_items = [item for item in items if isinstance(item, (int, float)) and not isinstance(item, bool)]
    if numeric_items:
        total = sum(numeric_items)
        average = total / len(numeric_items)
        print(f"平均值: {average}")
    else:
        print("平均值: 无数据")

    db_connection = await get_db_connection()
    if db_connection is not None:
        db_connection.commit()
    else:
        print("数据库连接不可用，跳过提交")

    return True


async def get_db_connection():
    """获取数据库连接。"""
    await asyncio.sleep(0)
    return None


async def save_to_db(data):
    """异步保存数据到数据库。"""
    await asyncio.sleep(0.1)
    print("数据已保存到数据库")


async def main():
    test_payload = {
        "event_type": "push",
        "user_id": 10086,
        "items": [],
        "is_critical": False
    }
    await process_webhook_event(test_payload)


if __name__ == '__main__':
    asyncio.run(main())
