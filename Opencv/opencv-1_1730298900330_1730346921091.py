import serial
import time

# 定义串口参数
port = 'COM3'  # 根据实际情况修改串口号
baud_rate = 9600  # 根据实际情况修改波特率
timeout = 1  # 超时时间

# 初始化串口
ser = serial.Serial(port, baud_rate, timeout=timeout)

# 确保串口已打开
if not ser.is_open:
    ser.open()

# 定义要发送的数据
QR_Data = "1234567890"  # 示例数据，实际使用时替换为你的 QR 数据

# 发送数据
ser.write(QR_Data.encode('utf-8'))

# 等待一段时间，确保数据发送完成
time.sleep(1)

# 读取响应
response = ser.read(ser.in_waiting or 1).decode('utf-8')

# 打印响应
print("收到的数据:", response)

# 关闭串口
ser.close()
