from EmailLib import SendEmail
class EmailConf(SendEmail.SendEmail):
    #这里可以定义多个email_conf方法用于不同的邮件发送
    def email_conf1(self):
            # 发件人
            self.from_e = '573734817@qq.com'
            # 收件人
            self.to = ['1326946283@qq.com', '3083460943@qq.com']
            # smtp服务器
            self.hostname = 'smtp.qq.com'
            # 发件人用户名
            self.username = '573734817@qq.com'
            # 发件人密码（授权码，不是登录密码）
            self.password = 'bmjslbtpdkkfbbjf'
            # 主题
            self.mailsubject = 'this is test'
            # 发送email的类型
            self.emailtype = 'html'
            # 正文（可以是text也可以是html）
            self.mailtext = '<html><body><h1>Hello</h1><p>send by <a href="http://www.python.org">Python</a>...</p></body></html>'
            # 编码方式
            self.mailencoding = 'utf-8'
            # 附件相关配置
            # 附件类型
            self.annextype = 'image'
            # 附件路径
            self.annexpath = './imgs/test.jpg'
            # 附件名称包含后缀名
            self.annexname = 'test.jpg'
            # 附件后缀
            self.annexsuffix = 'jpg'
            #下面这两条语句效果一样
            #SendEmail.SendEmail().send_email()
            self.send_email()

