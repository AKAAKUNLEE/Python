import qrcode
import pandas as pd
import os

def generate_qr_code(data, output_dir, size=80):
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 读取CSV文件
    df = pd.read_csv(data)

    # 遍历每一行数据
    for index, row in df.iterrows():
        Sequence = row['Sequence']
        First = row['First']

        # 生成二维码
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(First)
        qr.make(fit=True)

        # 创建二维码图像
        img = qr.make_image(fill='black', back_color='white')

        # 调整图像大小
        img = img.resize((size, size))

        # 保存二维码图像
        filename = f"{output_dir}/qr_code_{Sequence}.png"
        img.save(filename)
        print(f"QR code generated and saved to {filename}")

if __name__ == "__main__":
    data_file = 'output.csv'
    output_directory = 'qrcodes'
    qr_size = 80
    generate_qr_code(data_file, output_directory, qr_size)