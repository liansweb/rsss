"""
解析RSS feed
"""

from src.start import script
logger = script.logger

OPERATION_KEY = 'operation'
LINK_KEY = 'link'
ANALYSIS_KEY = 'analysis'
PRIORITY_KEY = 'priority'
OMPL_KEY = 'ompl'
NAME_KEY = 'name'


# TODO：支持多种脚本
def __package_python(pcakage):
    """
    A function that appends '.py' to the input package name and returns the result.
    """
    return pcakage + '.py'

def get_function(file_path,package,*args):
    """
    反射获取方法
    
    filepath  文件路径
    package  文件名/类名/方法名相同
    
    返回获取到的方法
    """
    # 使用 module_from_spec 创建一个模块对象
    from importlib.util import spec_from_file_location, module_from_spec
    
    spec = spec_from_file_location("custom_module", file_path)
    
    module = module_from_spec(spec)
    
    # 执行模块代码
    spec.loader.exec_module(module)
    
    # 获取模块的字典表示
    module_dict = vars(module)
    
    # 检查模块中是否有指定的属性或子模块
    if package in module_dict:
        package_class = module_dict[package]
        try:
            package_function = getattr(package_class, package)
            logger.info(f"[*] {args[0]}获取成功")
        except Exception:
            logger.info(f"[*] 在 [{package}] 类中找不到名为 [{package}] 方法")
    else:
        logger.error(f"[*] 在 [{__package_python(package)}] 文件中找不到名为 [{package}] 的类")
        return None
    
    
    return package_function

def get_operation(package):
    """
    获取操作器
    
    Args:
        package (str): 操作器的名称
        
    Returns:
        function or None: 返回操作器函数，如果找不到则返回 None
    """
    
    from src.rss.operation import OPERATION_LIST
    import os
    
    # 检查操作器是否存在于操作器列表中
    if __package_python(package) not in OPERATION_LIST:
        logger.error(f'[*] 无法找到名为 [{package}] 的操作器')
        return None
        
    from src.rss import operation
    
    # 获取操作器文件的绝对路径
    file_path = os.path.abspath(os.path.join(operation.__path__[0], __package_python(package)))
    
    
    
    package_function = get_function(file_path, package, '操作器')
    
    return package_function


def get_link():
    """
    获取RSSlink
    """

def get_ompl():
    """
    获取ompl地址
    """

def get_analysis(package):
    """
    获取ompl解析器
    """
    from src.rss.analysis import ANALYSIS_LIST
    import os
    
    if __package_python(package) not in ANALYSIS_LIST:
        logger.error(f'[*] 无法找到名为 [{package}] 的解析器')
        return None
    
    from src.rss import analysis
    
    file_path = os.path.abspath(os.path.join(analysis.__path__[0], __package_python(package)))

    package_function = get_function(file_path, package, '解析器')
    
    return package_function

def get_priority(priority_list, *args) -> list:
    """
    获取优先级
    """
    # 在原列表上添加优先级数字
    priority_list.append(args[0])
    
    # 对列表进行排序，这里使用了内置的排序方法
    priority_list.sort()
    
    # 返回排序后的列表
    return priority_list[::-1]

def get_item(RSS_LIBRARY) -> list:
    """
    返回排序后的项目
    """
    priority_list = []
    
    logger.info(f"[*] 仓库优先级排序") 
    # 先对项目排序
    for key in RSS_LIBRARY.keys():
        
        # 优先级排序
        if len(priority_list) == 0:
            priority_list.append(RSS_LIBRARY[key].get(PRIORITY_KEY))
        else:
            priority_list = get_priority(priority_list,RSS_LIBRARY[key].get(PRIORITY_KEY))

    # 排序后的RSS资源
    opml_list = []
    for i in priority_list:
        for key in RSS_LIBRARY.keys():
            if i == RSS_LIBRARY[key].get(PRIORITY_KEY):
                rss_library = RSS_LIBRARY[key]
                rss_library['name'] = key
                opml_list.append(rss_library)
    logger.debug(opml_list)
    
    opml_return_list = []
    
    # 开始构建RSS操作器
    for item in opml_list:
        
        # 获取操作器
        reflect_operation_function =  get_operation(item.get(OPERATION_KEY))

        # 操作器为空就跳过
        if reflect_operation_function is None:
            continue

        # 获取仓库名
        opml_name = item[NAME_KEY]
        logger.info(f"[*] 操作 [{opml_name}] 仓库")
        
        # 获取链接
        reflect_operation_function_path = item.get(LINK_KEY)
        
        # 获取内容
        opml_content =reflect_operation_function(PATH=reflect_operation_function_path)
        
        # 获取解析器
        # operation/get_opml.py
        reflect_analysis_function = get_analysis(item.get(ANALYSIS_KEY))
                 
        # 解析器为空就跳过         
        if reflect_analysis_function is None:
            continue
        
        # 获取解析后的内容
        # analysis/opml.py
        logger.info(f"[*] 解析ompl [{opml_name}]")
        opml_analysis_content = reflect_analysis_function(content=opml_content)
        
        opml_return_list.append(opml_analysis_content)
    
    logger.debug(f"[*] 解析后数据 {opml_return_list}")
    
    return  opml_return_list    
    
      
def action_main(**keywords):
    """
    A function that performs the main action using the provided keywords as parameters.
    """
    RSS_LIBRARY = keywords['RSS_LIBRARY']
    logger.debug(f"[*] ompl配置信息 {RSS_LIBRARY}")
    opml_rss_link = get_item(RSS_LIBRARY)
    
    return opml_rss_link