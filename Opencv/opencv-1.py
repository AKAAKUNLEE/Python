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
for QR in QR_code:
    QR_Data = QR.data.decode('utf-8')
    point = QR.rect
    cv2.rectangle(img, (point[0], point[1]), (point[0] + point[2], point[1] + point[3]), (0, 255, 0), 5)
    cv2.putText(img, QR_Data, (point[0] - 20, point[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# 显示图像
cv2.imshow('QR Code Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
