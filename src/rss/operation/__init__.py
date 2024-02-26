"""
操作器模块：
    1. 可以自定义操作器
    2. 文件名/类名/方法名必需一致。
"""

# coding: utf-8
import os
from src.start import script
logger = script.logger

# 获取文件路径
OPERATION_ADDR = os.path.dirname(os.path.realpath(__file__))
# 获取操作器的列表
OPERATION_LIST = []

def __operation_list(module_path):
    """
    列出指定模块路径下的所有文件和子目录
    """
    
    logger.info("[*] 注册操作器")
    if os.path.exists(module_path) and os.path.isdir(module_path):
        # 使用 os.listdir 获取目录下的所有文件和目录
        files_and_directories = os.listdir(module_path)
        
        # 过滤出文件
        files = [f for f in files_and_directories if os.path.isfile(os.path.join(module_path, f))]
                
        # 过滤出目录
        directories = [d for d in files_and_directories if os.path.isdir(os.path.join(module_path, d))]
        
        return files, directories
    else:
        return None

def __init__():

    result = __operation_list(OPERATION_ADDR)
    if result:
        files, directories = result
        
        logger.debug("Files in the module:", files)
        logger.debug("Directories in the module:", directories)
    else:
        logger.info("[*] 操作器获取失败")
    return files

OPERATION_LIST = __init__()