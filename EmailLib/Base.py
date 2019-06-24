import logging
import time
class Base(object):
    # 定义构造函数，定义各种属性和logging类的配置
    def __init__(self):
        # 发件人
        self.from_e = ''
        # 收件人
        self.to = ()
        # smtp服务器
        self.hostname = ''
        # 发件人用户名
        self.username = ''
        # 发件人密码（授权码，不是登录密码）
        self.password = ''
        # 主题
        self.mailsubject = ''
        # 发送email的类型
        self.emailtype = ''
        # 正文（可以是text也可以是html）
        self.mailtext = ''
        # 编码方式
        self.mailencoding = ''
        # 附件相关配置
        # 附件类型
        self.annextype = ''
        # 附件路径
        self.annexpath = ''
        # 附件名称包含后缀名
        self.annexname = ''
        # 附件后缀
        self.annexsuffix = ''

        logging.basicConfig(level=logging.WARNING,  # 控制台打印的日志级别 DEBUG WARNING
                            filename='./log/' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log',
                            filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                            # a是追加模式，默认如果不写的话，就是追加模式
                            format=
                            '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                            # 日志格式
                            )