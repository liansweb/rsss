# coding: utf-8


print("[✅]start")


class script:
    """
    设置ini常量
    """
    
    # 设置初始化
    
    LOG_LEVEL = ''
    logger = ''
    DATABASE_NAME = ''
    TABLE_NAME = ''
    
    # RSS仓库初始化
    RSS_LIBRARY = {}
    
    def __init__(self,**keywords):
        
        from src.config.get import get_value
        from src.config.get import transform 
        script.LOG_LEVEL = get_value(keywords['CONFIG_INI'],'log','level','info')
        script.logger = self._set_log()
        script.DATABASE_NAME = get_value(keywords['CONFIG_INI'],'database','database_name')
        script.TABLE_NAME = get_value(keywords['CONFIG_INI'],'database','table_name')
        script.RSS_LIBRARY = transform(keywords['OPML_INI'])
        
        
        
    def _set_log(self):
        from src.log import LoggerConfigurator
        return LoggerConfigurator.configure_logger(script.LOG_LEVEL)
    
class handle:
    """
    执行任务
    """
    
    def __init__(self):
        """
        core初始化
        """
        self.RSS_LIBRARY = script.RSS_LIBRARY
    
    def rss_handle(self,RSS_LIBRARY):
        """
        rss处理器
        """
        from src.rss.action import action_main
        keywords = {
            'RSS_LIBRARY':RSS_LIBRARY
        }
        
        return action_main(**keywords)
        
    
    def persistent_handle(self):
        """
        persistent处理器
        """
        
        
    def request_handle(self):
        """
        request处理器
        """
    
    def analysis_handle(self):
        """
        analysis处理器
        """
    
    def notify_handle(self):
        """
        notify处理器
        """
    
    def AI_handle(self):
        """
        AI处理器
        """
        # Implement your method here
        pass
    
    def core(self):
        """
        main流程操作
        """
        opml_rss_link = self.rss_handle(self.RSS_LIBRARY)
        self.persistent_handle(opml_rss_link)
        pass
    