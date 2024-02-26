"""
获取本地RSS feed
"""

class get_opml:

    @staticmethod
    def get_opml(PATH):
        
        from src.start import script
        logger = script.logger        
        
        """
        This function parses a local opml file
        """
        with open(PATH, 'r') as file:
            opml = file.read()
        logger.info(f'[*] 读取本地opml文件 [{PATH.split("/")[-1]}]')
        return opml
