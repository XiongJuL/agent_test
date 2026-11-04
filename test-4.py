def analyze_data(data_list):
    print("--- 开始分析数据 ---")
    
    # 错误 1：缩进错误 (IndentationError)
    # 仔细看这一行的开头，多了一个空格
     total_items = len(data_list)
    print(f"总共接收到 {total_items} 条数据")

    # 错误 2：索引越界 (IndexError)
    # 列表明明只有 3 个元素，非要去拿第 4 个
    fourth_item = data_list[3] 
    print(f"第 4 个元素是: {fourth_item}")

    # 错误 3：类型转换错误 (ValueError)
    # 试图把带中文的字符串转换成数字
    score = int("100分") 
    print(f"分数是: {score}")

    # 错误 4：属性错误 (AttributeError)
    # 列表 (list) 没有 keys() 这个方法，字典 (dict) 才有
    all_keys = data_list.keys() 
    print(f"所有键: {all_keys}")

    # 错误 5：文件找不到错误 (FileNotFoundError)
    # 试图读取一个不存在的日志文件
    with open("app_log.txt", "r", encoding="utf-8") as f:
        log_content = f.read()

    # 错误 6：局部变量未绑定 (UnboundLocalError)
    # 在函数内部修改外部变量，但没声明 global
    counter = 0
    def add_count():
        counter += 1
    
    add_count()
    print(f"计数器: {counter}")

    return total_items

# 测试数据
my_data = ["苹果", "香蕉", "橘子"]
analyze_data(my_data)
