import csv

def merge_cells(input_file, output_file, row_index, col1, col2, col3):
    """
    合并指定行的三个单元格，并生成新的CSV文件。

    :param input_file: 输入的CSV文件路径
    :param output_file: 输出的CSV文件路径
    :param row_index: 要合并的行索引（从0开始）
    :param col1: 第一个单元格的列索引（从0开始）
    :param col2: 第二个单元格的列索引（从0开始）
    :param col3: 第三个单元格的列索引（从0开始）
    """
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows = list(reader)

    # 检查行和列索引是否有效
    if row_index >= len(rows) or col1 >= len(rows[row_index]) or col2 >= len(rows[row_index]) or col3 >= len(rows[row_index]):
        raise IndexError("指定的行或列索引超出范围")

    # 合并指定行的三个单元格
    merged_value = rows[row_index][col1] + rows[row_index][col2] + rows[row_index][col3]
    rows[row_index][col1] = merged_value
    del rows[row_index][col2]
    del rows[row_index][col3 - 1]  # 因为删除了一个列，所以需要调整索引

    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)

    print(f"已成功生成新的CSV文件: {output_file}")

input_file = 'permutations_with_plus.csv'
output_file = 'output.csv'
row_index = 0
col1 = 0
col2 = 1
col3 = 2

merge_cells(input_file, output_file, row_index, col1, col2, col3)    