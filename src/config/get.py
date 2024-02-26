# coding=utf-8
import configparser
config = configparser.ConfigParser()


def get_value(filename,section_name,key,default=None):
    """
    获取变量值
    """
    import logging
    from src.start import script

    # 如果 script.LOG_LEVEL 为空，创建新的 logger
    if script.LOG_LEVEL == '':
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s'
        )
        logger = logging.getLogger(__name__)
    else:
        logger = script.logger

    
    config.read(filename, encoding='utf-8')
    value = config.get(section_name, key, fallback=default)
    config.clear()
    logger.info(f'获取[{filename}], section[{section_name}], key[{key}]')
    return value

def check_value():
    """
    检查是否存在
    """
    print

def set_value(filename,section_name,key,value):
    """
    设置变量
    """
    pass

def transform(*args) -> dict:
    """
    将configparser 转化 python dict
    """
    config.read(args[0])
    # 将配置项转换为 Python 字典
    config_dict = {section: dict(config.items(section)) for section in config.sections()}
    config.clear()
    return config_dict

def get_sections(filename: str) -> list:
    """
    获取配置根节点
    """
    config.read(filename,encoding='utf-8')
    sections = config.sections()
    # logger.info(f'获取[{filename}]')
    
    return sections

def test():
    from src.start import script
    # script.logger.info(f'{dir(script)}')
    # print(script.RSS_LIBRARY)
    # print(script.logger.info)
    pass
    