import csv
def merge_cells_with_sequence(input_file, output_file, col1, col2, col3):
    """
    在第二行开始的左侧插入序列号，并合并指定的三个单元格，生成新的CSV文件。

    :param input_file: 输入的CSV文件路径
    :param output_file: 输出的CSV文件路径
    :param col1: 第一个单元格的列索引（从0开始）
    :param col2: 第二个单元格的列索引（从0开始）
    :param col3: 第三个单元格的列索引（从0开始）
    """
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows = list(reader)

    # 检查列索引是否有效
    for row in rows[1:]:  # 从第二行开始检查
        if col1 >= len(row) or col2 >= len(row) or col3 >= len(row):
            raise IndexError("指定的列索引超出范围")

    # 插入序列号并合并单元格
    for i, row in enumerate(rows[1:], start=1):  # 从第二行开始，序列号从1开始
        row.insert(0, str(i))  # 在每行的最左侧插入序列号
        merged_value = row[col1 + 1] + row[col2 + 1] + row[col3 + 1]  # 调整列索引
        row[col1 + 1] = merged_value
        del row[col2 + 1]
        del row[col3]  # 因为删除了一个列，所以需要调整索引

    # 将表头行也插入序列号列
    header = rows[0]
    header.insert(0, "Sequence")

    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)

    print(f"已成功生成新的CSV文件: {output_file}")

input_file = 'permutations_with_plus.csv'
output_file = 'output.csv'
col1 = 0
col2 = 1
col3 = 2

merge_cells_with_sequence(input_file, output_file, col1, col2, col3)