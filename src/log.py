import logging

class LoggerConfigurator:
    @staticmethod
    def configure_logger(level):
        # 设置一个格式化字符串，它将用于所有的日志级别
        standard_format = '%(asctime)s - %(module)s - %(funcName)s - %(lineno)d - '
        debug_format = '[%(pathname)s:%(lineno)d] - %(module)s - %(funcName)s - %(lineno)d - '
        message_format = '%(message)s'
        # 确定日志级别的格式化输出
        if level == "DEBUG":
            # DEBUG 级别包含更丰富的上下文信息
            format = standard_format + debug_format + message_format
        elif level in {"INFO", "WARNING", "ERROR", "CRITICAL"}:
            # 其他级别保持一致的简要信息
            format = standard_format + message_format
        else:
            # 默认设置为 INFO 级别
            level = "INFO"
            format = standard_format + message_format
        
                
        logger = logging.getLogger(__name__)
        logger = logging.getLogger(level)
        logger.setLevel(level)

        formatter = logging.Formatter(format)

        handler = logging.StreamHandler()
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.propagate = False

        return logger

