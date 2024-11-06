import itertools
import pandas as pd

def generate_permutations():
    # 定义数字列表
    numbers = [1, 2, 3]

    # 生成所有可能的排列
    permutations = list(itertools.permutations(numbers))

    # 生成排列组合
    combinations = []
    for perm in permutations:
        # 将排列转换为字符串形式
        forward = ''.join(map(str, perm))
        reverse = ''.join(map(str, reversed(perm)))
        combinations.append((forward, reverse))

    # 将组合转换为DataFrame
    df = pd.DataFrame(combinations, columns=['Forward', 'Reverse'])

    # 保存到CSV文件
    output_file = 'permutations.csv'
    df.to_csv(output_file, index=False)
    print(f"Permutations saved to {output_file}")

if __name__ == "__main__":
    generate_permutations()
    