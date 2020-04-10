from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage
import smtplib
import configparser


# 读取配置文件
cf = configparser.ConfigParser()
cf.read('conf.ini', encoding='utf-8')
secs = cf.sections()
opts = cf.options('email')

print(secs, opts)

host = cf.get('email', 'mail_host')
port = cf.get('email', 'port')
user = cf.get('email', 'mail_name')
mail_pass = cf.get('email', 'mail_pass')
receiver = cf.get('email', 'receiver')
content = cf.get('email', 'content')
subject = cf.get('email', 'subject')
receiver_name = cf.get('email', 'receiver_name')

class sendEMail(object):
    """封装发送邮件类"""

    def __init__(self):
        """第一步：连接到smtp服务器"""
        self.smtp_s = smtplib.SMTP(host=host,
                                   port=port)
        """第二步：登录到smtp服务器"""
        self.smtp_s.login(user=user,
                          password=mail_pass)

    def send_mail(self):
        """
        发送邮件
        对方的邮箱，内容，标题都
        取自配置文件

        """

        # receiver = cf.get('email', 'receiver')
        # content = cf.get('email', 'content')
        # subject = cf.get('email', 'subject')
        msg = MIMEMultipart('related')
        msg['from'] = Header(user, 'UTF-8')
        msg['to'] = ";".join(receiver)             # Header(receiver, 'utf-8')
        # msg['cc'] = Header('alexle@x2era.com', 'UTF-8')
        msg['subject'] = Header(subject, 'utf-8')

        msg2 = MIMEMultipart('alternative')
        msg.attach(msg2)
        # 添加图片

        msg2.attach(MIMEText(content, 'html', 'utf-8'))
        msgImag = MIMEImage(open('picture.jpg', 'rb').read())
        msgImag.add_header('Content-ID', '<image1>')
        msg.attach(msgImag)

        # 添加附件
        att1 = MIMEText(open('newV_punch.py', 'rb').read(), 'base64', 'utf-8')
        att1['content-type'] = 'application/octet-stream'
        att1['content-disposition'] = 'attachment; filename = "newV_punch.py"'
        msg2.attach(att1)

        # 发送邮件
        try:
            self.smtp_s.sendmail(user, receiver, msg.as_string())
            self.smtp_s.quit()
            print('邮件发送成功')
            return True
        except smtplib.SMTPException as e:
            print('邮件发送失败！')
            print(e)
            return False


if __name__ == '__main__':

    a = sendEMail()
    a.send_mail()








