1���ò������Ϊ�����ʼ���
2������python��д��
3��ʹ�õ�ʱ��ֻ��Ҫ���ú�Emailconf�ļ����ɡ�
����demo���£�
	    # ������
	    self.from_e = '573734817@qq.com'
            # �ռ���
            self.to = ('1326946283@qq.com')
            # smtp������
            self.hostname = 'smtp.qq.com'
            # �������û���
            self.username = '573734817@qq.com'
            # ���������루��Ȩ�룬���ǵ�¼���룩
            self.password = 'bmjslbtpdkkfbbjf'
            # ����
            self.mailsubject = 'this is test'
            # ����email������
            self.emailtype = 'html'
            # ���ģ�������textҲ������html��
            self.mailtext = '<html><body><h1>Hello</h1><p>send by <a href="http://www.python.org">Python</a>...</p></body></html>'
            # ���뷽ʽ
            self.mailencoding = 'utf-8'
            # �����������
            # ��������
            self.annextype = 'image'
            # ����·��
            self.annexpath = './imgs/test.jpg'
            # �������ư�����׺��
            self.annexname = 'test.jpg'
            # ������׺
            self.annexsuffix = 'jpg'
����self.to��һ�����飨tuple���������Ļ��Ϳ��Է��͸�����ˡ�

4�������Ҫ����ķ����˷�����ͬ���ռ��˵Ļ����������ö��def email_conf3(self):
   Ȼ������Run.py�����������伴��
   EmailConf.EmailConf().email_conf3()