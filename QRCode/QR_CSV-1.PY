import itertools
import pandas as pd

def generate_permutations_no_repeat():
    # 定义数字列表
    numbers = [1, 2, 3]

    # 生成所有可能的排列（数字不允许重复）
    permutations = list(itertools.permutations(numbers))

    # 生成排列组合
    combinations = []
    for perm1 in permutations:
        for perm2 in permutations:
            # 将排列转换为字符串形式
            forward1 = ''.join(map(str, perm1))
            forward2 = ''.join(map(str, perm2))
            combinations.append((forward1, forward2))

    # 将组合转换为DataFrame
    df = pd.DataFrame(combinations, columns=['First', 'Second'])

    # 保存到CSV文件
    output_file = 'permutations_no_repeat.csv'
    df.to_csv(output_file, index=False)
    print(f"Permutations without repetition saved to {output_file}")

if __name__ == "__main__":
    generate_permutations_no_repeat()