#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：url快速转换快捷方式.py
@File    ：opencv-1.py
@IDE     ：PyCharm
@Author  ：AKUNLEE
@Date    ：2024/10/29 17:54
"""
import cv2
from pyzbar.pyzbar import decode
import re

img = cv2.imread('text.jpg')
QR_code = decode(img)



# 打开或创建文件，准备写入（如果文件存在则覆盖）
# with open('QR_Data_cleaned.txt', 'w', encoding='utf-8') as file:
for QR in QR_code:
    QR_Data = QR.data.decode('utf-8')
    QR_Data_cleaned = re.sub(r'\+', '', QR_Data)
    point = QR.rect
    cv2.rectangle(img, (point[0], point[1]), (point[0] + point[2], point[1] + point[3]), (0, 255, 0), 5)
    cv2.putText(img, QR_Data, (point[0] - 20, point[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

'''     # 将 QR_Data 写入文件
        file.write(QR_Data_cleaned + '\n')
        '''

characters = list(QR_Data_cleaned)
def map_characters_to_colors(characters):
    color_map = {
        '1': 'red',
        '2': 'green',
        '3': 'blue'
    }
    mapped_characters = [color_map.get(char, char) for char in characters]
    return mapped_characters

'''# 显示图像
cv2.imshow('QR Code Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
mapped_characters = map_characters_to_colors(characters)
print(mapped_characters)