from EmailLib import Base
import logging
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class SendEmail(Base.Base):
    def send_email(self):
        try:
            smtp = SMTP_SSL(self.hostname)
            smtp.set_debuglevel(1)
            smtp.ehlo(self.hostname)

            smtp.login(self.username, self.password)

            msg = MIMEMultipart()
            msg.attach(MIMEText(self.mailtext, self.emailtype, self.mailencoding))
            msg["Subject"] = Header(self.mailsubject, self.mailencoding)
            msg["from"] = self.from_e
            #msg["to"] = self.to
            if self.annexpath != "":
                with open(self.annexpath, 'rb') as f:
                    # 设置附件的MIME和文件名，这里是png类型:
                    mime = MIMEBase(self.annextype, self.annexsuffix, filename=self.annexname)
                    # 加上必要的头信息:
                    mime.add_header('Content-Disposition', 'attachment', filename=self.annexname)
                    mime.add_header('Content-ID', '<0>')
                    mime.add_header('X-Attachment-Id', '0')
                    # 把附件的内容读进来:
                    mime.set_payload(f.read())
                    # 用Base64编码:
                    encoders.encode_base64(mime)
                    # 添加到MIMEMultipart:
                    msg.attach(mime)

            smtp.sendmail(self.from_e, self.to, msg.as_string())

            smtp.quit()
        except Exception as e:
            logging.exception(e)
