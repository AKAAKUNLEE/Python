import cv2
import numpy as np

# 相机参数
focal_length = 800  # 焦距（单位：像素）
baseline = 60  # 基线距离（单位：毫米）
pixel_size = 0.003  # 像素大小（单位：毫米）

# 初始化摄像头
cap_left = cv2.VideoCapture(0)
cap_right = cv2.VideoCapture(1)

# 设置摄像头分辨率
cap_left.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap_left.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
cap_right.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap_right.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

if not cap_left.isOpened() or not cap_right.isOpened():
    print("无法打开摄像头")
    exit()

while True:
    ret_left, frame_left = cap_left.read()
    ret_right, frame_right = cap_right.read()

    if not ret_left or not ret_right:
        print("无法读取帧")
        break

    # 显示原始图像
    cv2.imshow('Left Camera', frame_left)
    cv2.imshow('Right Camera', frame_right)

    # 转换为灰度图像
    gray_left = cv2.cvtColor(frame_left, cv2.COLOR_BGR2GRAY)
    gray_right = cv2.cvtColor(frame_right, cv2.COLOR_BGR2GRAY)

    # 计算视差图
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    disparity = stereo.compute(gray_left, gray_right)

    # 归一化视差图
    disparity_normalized = cv2.normalize(disparity, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # 显示视差图
    cv2.imshow('Disparity Map', disparity_normalized)

    # 计算深度图
    depth_map = (focal_length * baseline) / (disparity + 1e-7)  # 避免除零错误

    # 显示深度图
    depth_map_normalized = cv2.normalize(depth_map, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    cv2.imshow('Depth Map', depth_map_normalized)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap_left.release()
cap_right.release()
cv2.destroyAllWindows()
