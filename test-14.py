import asyncio


async def save_to_db(payload):
    """异步保存数据到数据库（占位实现）。"""
    # TODO: 实现实际的数据库保存逻辑
    return True


def commit_transaction(db_connection):
    """提交事务：先检查数据库连接是否可用。"""
    if db_connection is not None:
        db_connection.commit()
    else:
        raise RuntimeError("数据库连接不可用，无法提交事务")


def calculate_average(items):
    """计算平均值：先判断 items 是否为空，避免除零错误。"""
    if items:
        total = sum(items)
        average = total / len(items)
    else:
        total = 0
        average = 0
    return total, average


def is_critical_event(payload):
    """判断是否为关键事件：先做类型检查再取值。"""
    return isinstance(payload, dict) and bool(payload.get("is_critical"))


def get_event_name(payload):
    """获取事件名称：先做类型检查再取值。"""
    return payload.get("event_type") if isinstance(payload, dict) else None


async def process_event(payload, items=None, db_connection=None):
    """处理事件的主流程。"""
    items = items or []

    # 计算平均值
    total, average = calculate_average(items)

    # 异步保存数据到数据库
    await save_to_db(payload)

    # 判断是否为关键事件
    if is_critical_event(payload):
        # 关键事件处理逻辑
        pass

    # 获取事件名称
    event_name = get_event_name(payload)

    # 提交事务
    commit_transaction(db_connection)

    return {
        "total": total,
        "average": average,
        "event_name": event_name,
    }


class _DummyConnection:
    def commit(self):
        pass


if __name__ == "__main__":
    asyncio.run(process_event({"event_type": "test", "is_critical": False}, db_connection=_DummyConnection()))
