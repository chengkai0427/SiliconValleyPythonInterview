
import json

# Python字典与JSON互相转换
user_data = {
    "name": "John Doe",
    "age": 30,
    "email": "john@example.com",
    "hobbies": ["reading", "swimming", "coding"]
}

# 转换为JSON字符串
json_str = json.dumps(user_data, indent=2)
print(json_str)

# 从JSON字符串解析为字典
parsed_data = json.loads(json_str)
print(parsed_data["name"])