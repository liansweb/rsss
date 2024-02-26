class opml:
    @staticmethod
    def opml(content) -> dict:
        """
        Parse the XML data in the given string and convert it to a Python dictionary representing the OPML structure.
        :param DATA: The XML data string
        :return: The Python dictionary representing the OPML structure
        """

        import xml.etree.ElementTree as ET
        from src.start import script
        logger = script.logger

        logger.debug(f"[*] 解析前内容 {content}")
        
        # DATA = '''<?xml version="1.0" encoding="UTF-8"?>
        # <opml version="1.0">
        #     <head>
        #         <title>Chinese-Security-RSS</title>
        #     </head>
        #     <body>
        #     <outline text="FreeBuf互联网安全新媒体平台" title="FreeBuf互联网安全新媒体平台" type="rss" xmlUrl="https://www.freebuf.com/feed" htmlUrl="https://www.freebuf.com"/>
        #     <outline text="安全客" title="安全客" type="rss" xmlUrl="https://api.anquanke.com/data/v1/rss" htmlUrl="https://www.anquanke.com"/>
        #     </body>
        # </opml>'''

        # Parse the XML
        root = ET.fromstring(content)

        # Convert XML to Python dict
        rss_dict = {
            "opml": {
                "version": root.get("version"),
                "head": {
                    "title": root.find("head/title").text
                },
                "body": {
                    "outlines": [
                        {
                            "text": outline.get("text"), 
                            "title": outline.get("title"),
                            "type": outline.get("type"),
                            "xmlUrl": outline.get("xmlUrl"),
                            "htmlUrl": outline.get("htmlUrl")
                        } for outline in root.find("body").findall("outline")
                    ]
                }
            }
        }

        logger.debug(f"[*] 解析后内容 {rss_dict}")
        
        return rss_dict

"""
生成示例：
{
    'opml': {
        'version': '1.0',
        'head': {'title': 'Chinese-Security-RSS'},
        'body': {
            'outlines': [
                {
                    'text': 'FreeBuf互联网安全新媒体平台',
                    'title': 'FreeBuf互联网安全新媒体平台',
                    'type': 'rss',
                    'xmlUrl': 'https://www.freebuf.com/feed',
                    'htmlUrl': 'https://www.freebuf.com'
                },
                {
                    'text': '安全客',
                    'title': '安全客',
                    'type': 'rss',
                    'xmlUrl': 'https://api.anquanke.com/data/v1/rss',
                    'htmlUrl': 'https://www.anquanke.com'
                }
            ]
        }
    }
}

"""