1、该插件功能为发送邮件。
2、基于python编写。
3、使用的时候只需要配置好Emailconf文件即可。
配置demo如下：
	    # 发件人
	    self.from_e = '573734817@qq.com'
            # 收件人
            self.to = ('1326946283@qq.com')
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
其中self.to是一个数组（tuple），这样的话就可以发送给多个人。

4、如果需要多个的发件人发给不同的收件人的话，可以配置多个def email_conf3(self):
   然后再在Run.py中添加运行语句即可
   EmailConf.EmailConf().email_conf3()