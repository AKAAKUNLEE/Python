import csv
def merge_cells(input_file, output_file, col1, col2, col3):
    """
    合并除第一行外的每一行的三个单元格，并生成新的CSV文件。

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

    # 合并除第一行外的每一行的三个单元格
    for row in rows[1:]:  # 从第二行开始合并
        merged_value = row[col1] + row[col2] + row[col3]
        row[col1] = merged_value
        del row[col2]
        del row[col3 - 1]  # 因为删除了一个列，所以需要调整索引

    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)

    print(f"已成功生成新的CSV文件: {output_file}")

input_file = 'permutations_with_plus.csv'
output_file = 'output.csv'
col1 = 0
col2 = 1
col3 = 2

merge_cells(input_file, output_file, col1, col2, col3)    