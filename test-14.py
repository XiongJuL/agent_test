# 文件: test-14.py:37
event_name = payload.get("event_type")

# 文件: test-14.py:34
print("items 为空，无法计算平均值")

# 文件: test-14.py:33
else:

# 文件: test-14.py:32
print(f"平均值: {average}")

# 文件: test-14.py:31
average = total / len(items)

# 文件: test-14.py:30
# 删除重复的代码块

# 文件: test-14.py:27
if isinstance(payload, dict) and payload.get("is_critical"):

# 文件: test-14.py:24
await save_to_db(payload)

# 文件: test-14.py:22
print("items 为空，无法计算平均值")

# 文件: test-14.py:21
else:

# 文件: test-14.py:20
print(f"平均值: {average}")

# 文件: test-14.py:19
average = total / len(items)

# 文件: test-14.py:18
# 删除重复的代码块

# 文件: test-14.py:17
print("items 为空，无法计算平均值")

# 文件: test-14.py:16
else:

# 文件: test-14.py:15
print(f"平均值: {average}")

# 文件: test-14.py:14
average = total / len(items)

# 文件: test-14.py:13
if items:

# 文件: test-14.py:11
if items:
    pass

# 文件: test-14.py:10
raise RuntimeError("数据库连接不可用，无法提交事务")

# 文件: test-14.py:9
# 删除重复的 raise 语句

# 文件: test-14.py:8
# 删除重复的 commit 调用

# 文件: test-14.py:6
else:
        raise RuntimeError("数据库连接不可用，无法提交事务")

# 文件: test-14.py:5
if db_connection is not None:

# 文件: test-14.py:4
if db_connection is not None:
        db_connection.commit()
    else:
        raise RuntimeError("数据库连接不可用，无法提交事务")

# 文件: test-14.py:2
# 删除重复的赋值行

# 文件: test-14.py:1
welcome_msg = f"欢迎用户： {user_id}"  # 请确保 user_id 已定义，例如从参数传入

