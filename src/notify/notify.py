# 推送信息
PUSH = {
    
    # 飞书 webhook地址 示例：https://open.feishu.cn/open-apis/bot/v2/hook/****，使用：https://open.feishu.cn/document/client-docs/bot-v3/add-custom-bot
    'FHWEBHOOK': 'https://open.feishu.cn/open-apis/bot/v2/hook/' ,
    
    'QYWX_AM': '',                      # 企业微信应用
    'QYWX_KEY': '',                     # 企业微信机器人
    
    'DD_BOT_SECRET': '',                # 钉钉机器人的 DD_BOT_SECRET
    'DD_BOT_TOKEN': '',                 # 钉钉机器人的 DD_BOT_TOKEN    

}



# 过滤需要的信息
FILTER = {
    
    # 包含关键字
    'contains': [
            '安全',
            '漏洞',
            '分析',
            'CVE',
            'API',
            '研究',
            '复现',
            '技术',
        ]
    ,
    
    # 不包含关键字
    'not_contains': [
            '钓鱼攻击',
            '勒索'
        ],
    
    # 匹配关键字
    'match': [
            '0day|1day'        
    ]
    
}

# 获取最近两天的信息 day/minute/second
DATE = {
    'day': 2,
    'minute': 10,
    'second': 100
}
