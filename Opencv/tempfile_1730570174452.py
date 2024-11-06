import cv2
import numpy as np

# 相机焦距（单位：像素）
focal_length = 800  # 这个值需要根据实际情况调整

# 已知目标物体的实际宽度（单位：毫米）
known_width = 200  # 这个值需要根据实际情况调整

# 相机与目标物体的实际距离（单位：毫米），用于校准
known_distance = 600  # 这个值需要根据实际情况调整

def calculate_focal_length(known_distance, known_width, pixel_width):
    """
    计算焦距
    :param known_distance: 已知距离（单位：毫米）
    :param known_width: 已知宽度（单位：毫米）
    :param pixel_width: 目标在图像中的宽度（单位：像素）
    :return: 焦距（单位：像素）
    """
    return (known_width * known_distance) / pixel_width

def calculate_distance(focal_length, known_width, pixel_width):
    """
    计算距离
    :param focal_length: 焦距（单位：像素）
    :param known_width: 已知宽度（单位：毫米）
    :param pixel_width: 目标在图像中的宽度（单位：像素）
    :return: 距离（单位：毫米）
    """
    return (known_width * focal_length) / pixel_width

def detect_and_calculate_distance(image_path):
    # 读取图像
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 使用Canny边缘检测
    edges = cv2.Canny(gray, 50, 150)

    # 使用轮廓检测找到目标
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        for contour in contours:
            # 获取最小外接矩形
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # 计算目标在图像中的宽度
            pixel_width = w

            # 计算距离
            distance = calculate_distance(focal_length, known_width, pixel_width)
            print(f"Distance: {distance} mm")

    # 显示结果
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # 假设已知目标在图像中的宽度为100像素
    pixel_width = 100
    focal_length = calculate_focal_length(known_distance, known_width, pixel_width)

    # 检测目标并计算距离
    image_path = "path_to_your_image.jpg"
    detect_and_calculate_distance(image_path)
