import jieba

# 读取文件
file_path = 'QR_Data_cleaned.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# 使用jieba进行分词
words = jieba.lcut(content)

# 打印分词结果
print(words)
