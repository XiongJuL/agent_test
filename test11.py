import asyncio
import logging

EVENT_TYPE_KEY = "event_type"
USER_ID_KEY = "user_id"
ITEMS_KEY = "items"
IS_CRITICAL_KEY = "is_critical"

logger = logging.getLogger(__name__)


def validate_payload(payload):
    """校验 payload 必要字段，返回 (event_name, user_id) 或 None。"""
    event_name = payload.get(EVENT_TYPE_KEY)
    if event_name is None:
        logger.warning("缺少事件类型，无法处理")
        return None
    logger.info("事件类型: %s", event_name)

    user_id = payload.get(USER_ID_KEY)
    if user_id is None:
        logger.warning("缺少用户ID，无法处理")
        return None
    logger.info("欢迎用户: %s", user_id)
    return event_name, user_id


def log_critical_alert(payload):
    """若为严重警报则记录日志。"""
    if payload.get(IS_CRITICAL_KEY):
        logger.warning("⚠️ 这是一个严重警报！")


def calculate_average(items):
    """计算数值型 items 的平均值，无有效数据时返回 None。"""
    if not isinstance(items, (list, tuple)):
        logger.warning("items 字段不是可迭代列表，跳过平均值计算")
        return None
    numeric_items = [
        item for item in items
        if isinstance(item, (int, float)) and not isinstance(item, bool)
    ]
    if not numeric_items:
        return None
    return sum(numeric_items) / len(numeric_items)


async def commit_db(db_connection):
    """提交数据库事务。"""
    if db_connection is None:
        logger.warning("数据库连接不可用，跳过提交")
        return False
    db_connection.commit()
    return True


async def process_webhook_event(payload):
    """处理 Webhook 事件并保存到数据库。"""
    logger.info("收到 Webhook 事件，开始处理...")

    validated = validate_payload(payload)
    if validated is None:
        return False

    db_connection = await get_db_connection()
    if db_connection is None:
        logger.error("无法获取数据库连接，事件处理失败")
        return False

    try:
        await save_to_db(db_connection, payload)
        committed = await commit_db(db_connection)
        if not committed:
            logger.error("数据库提交失败，事件未持久化")
            return False
    except Exception:
        logger.exception("保存或提交数据库时发生异常")
        return False

    log_critical_alert(payload)

    items = payload.get(ITEMS_KEY, [])
    average = calculate_average(items)
    if average is None:
        logger.info("平均值: 无数据")
    else:
        logger.info("平均值: %s", average)

    return True


class _InMemoryDBConnection:
    """简单的内存数据库连接，用于演示持久化。"""

    def __init__(self):
        self.data = []
        self.committed = False

    def commit(self):
        self.committed = True


async def get_db_connection():
    """获取数据库连接。"""
    await asyncio.sleep(0)
    return _InMemoryDBConnection()


async def save_to_db(db_connection, data):
    """异步保存数据到数据库。"""
    await asyncio.sleep(0.1)
    db_connection.data.append(data)
    logger.info("数据已保存到数据库")


async def main():
    test_payload = {
        "event_type": "push",
        "user_id": 10086,
        "items": [],
        "is_critical": False
    }
    await process_webhook_event(test_payload)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
