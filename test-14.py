# 文件: test-14.py:37
event_name = payload.get("event_type") if isinstance(payload, dict) else None

# 文件: test-14.py:27
if isinstance(payload, dict) and payload.get("is_critical"):

# 文件: test-14.py:11
if items:
    total = sum(items)
    average = total / len(items)
else:
    total = 0
    average = 0

# 文件: test-14.py:14
average = total / len(items) if items else 0

# 文件: test-14.py:19
average = total / len(items) if items else 0

# 文件: test-14.py:1
# 文件: test-14.py

# 提交事务：先检查数据库连接是否可用
if db_connection is not None:
    db_connection.commit()
else:
    raise RuntimeError("数据库连接不可用，无法提交事务")

# 计算平均值：先判断 items 是否为空，避免除零错误
if items:
    total = sum(items)
    average = total / len(items)
else:
    average = 0

# 异步保存数据到数据库
await save_to_db(payload)

# 判断是否为关键事件：先做类型检查再取值
if isinstance(payload, dict) and payload.get("is_critical"):
    # 关键事件处理逻辑
    pass

# 获取事件名称：先做类型检查再取值
event_name = payload.get("event_type") if isinstance(payload, dict) else None
