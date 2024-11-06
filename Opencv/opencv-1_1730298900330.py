# 读取文件
file_path = 'QR_Data_cleaned.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# 将每个字符分隔开
characters = list(content)

# 打印分隔后的字符
print(characters)
