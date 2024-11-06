from selenium import webdriver
from selenium.webdriver.edge.service import service

# 创建 WebDriver 对象.指明使用Edge浏览器驱动
wd = webdriver.Edge(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')


# 调用 WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('www.byhy.net')
