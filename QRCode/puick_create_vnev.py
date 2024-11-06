import os
import subprocess
import sys

def check_python_version():
    """检查当前Python版本是否为3.12"""
    version = sys.version_info
    if version.major != 3 or version.minor != 12:
        print("当前Python版本不是3.12，请确保已安装Python 3.12。")
        return False
    return True

def install_virtualenv():
    """安装virtualenv"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "virtualenv"])
        print("virtualenv安装成功。")
    except subprocess.CalledProcessError as e:
        print(f"安装virtualenv失败: {e}")
        sys.exit(1)

def create_venv(env_name):
    """创建虚拟环境"""
    try:
        subprocess.check_call([sys.executable, "-m", "virtualenv", env_name])
        print(f"虚拟环境 {env_name} 创建成功。")
    except subprocess.CalledProcessError as e:
        print(f"创建虚拟环境失败: {e}")
        sys.exit(1)

def main():
    env_name = input("请输入虚拟环境的名称: ")
    
    if not check_python_version():
        print("请先安装Python 3.12。")
        sys.exit(1)
    
    try:
        subprocess.check_call([sys.executable, "-m", "virtualenv", "--version"])
    except subprocess.CalledProcessError:
        print("未检测到virtualenv，正在安装...")
        install_virtualenv()
    
    create_venv(env_name)

if __name__ == "__main__":
    main()