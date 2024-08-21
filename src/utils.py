# Add utility functions as needed
import json
from datetime import datetime, date


def filter_json_by_date_from(json_str, cutoff_date_str):
    """从什么时间期开始筛选"""
    # 解析输入的JSON字符串
    data = json_str
    if isinstance(json_str, str):
        data = json.loads(json_str)
    print("------->筛选前共" + str(len(data)) + "条数据")
    # 把乱七八糟的日期格式化字符串统一格式
    cutoff_date_str = convert_to_date(cutoff_date_str).strftime("%Y-%m-%dT%H:%M:%SZ")
    # 将cutoff_date_str转换为datetime对象
    cutoff_date = datetime.strptime(cutoff_date_str, "%Y-%m-%dT%H:%M:%SZ")

    # 过滤掉created_at晚于cutoff_date的项
    filtered_data = [item for item in data if
                     datetime.strptime(item['created_at'], "%Y-%m-%dT%H:%M:%SZ") >= cutoff_date]
    print("------->筛选出"+cutoff_date_str+"后的数据， 共"+str(len(filtered_data))+"条")

    return filtered_data
    # 将过滤后的数据转换回JSON字符串
    # return json.dumps(filtered_data)


def filter_json_by_date(json_str, cutoff_date_str):
    """到什么时候截至"""
    # 解析输入的JSON字符串
    data = json_str
    if isinstance(json_str, str):
        data = json.loads(json_str)
    print("------->筛选前共" + str(len(data)) + "条数据")
    # 把乱七八糟的日期格式化字符串统一格式
    cutoff_date_str = convert_to_date(cutoff_date_str).strftime("%Y-%m-%dT%H:%M:%SZ")
    # 将cutoff_date_str转换为datetime对象
    cutoff_date = datetime.strptime(cutoff_date_str, "%Y-%m-%dT%H:%M:%SZ")

    # 过滤掉created_at晚于cutoff_date的项
    filtered_data = [item for item in data if
                     datetime.strptime(item['created_at'], "%Y-%m-%dT%H:%M:%SZ") <= cutoff_date]
    print("------->筛选出" + cutoff_date_str + "前的数据， 共"+str(len(filtered_data))+"条")
    return filtered_data
    # 将过滤后的数据转换回JSON字符串
    # return json.dumps(filtered_data)


def convert_to_date(date_str):
    # 定义可能的日期格式
    date_formats = [
        "%Y-%m-%d",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S.%f"
    ]

    for fmt in date_formats:
        try:
            # 尝试解析日期字符串
            dt = datetime.strptime(date_str, fmt)
            # 返回 date 类型
            return dt
        except ValueError:
            continue

    # 如果所有格式都不匹配，抛出异常
    raise ValueError(
        "Invalid date format. Expected formats: YYYY-MM-DD, YYYY-MM-DDTHH:MM:SSZ, or YYYY-MM-DDTHH:MM:SS.ssssss")
