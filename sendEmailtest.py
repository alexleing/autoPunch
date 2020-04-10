from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage
import smtplib


class SendEmail(object):

    def __init__(self,
                 mail_host,
                 port,
                 mail_name,
                 user_name,
                 mail_pass,
                 receiver,
                 receiver_name,
                 subject,
                 content,
                 file=None):

        self.mail_host = mail_host
        self.port = port
        self.mail_name = mail_name
        self.user_name = user_name
        self.mail_pass = mail_pass
        self.receiver = receiver
        self.receiver_name = receiver_name
        self.subject = subject
        self.content = content
        self.file = file

    def mail_content(self):

        if self.file != None:
            # 添加附件，提供下载
            msg = MIMEMultipart('related')
            with open(self.file, 'rb')as fp:
                content = fp.read()
            att = MIMEText(content, 'base64', 'utf-8')
            att['content-type'] = 'application/octet-stream'
            att['content-disposition'] = 'attachment; filename = "%s"' % self.file
            msg.attach(att)
            # for i in range(len(self.receiver)):

            # 添加图片，显示在邮件文本里面
            msg2 = MIMEMultipart('alternative')
            msg.attach(msg2)
            msgImage = MIMEImage(open('picture.jpg', 'rb').read())
            msgImage.add_header("Content-ID", "<image1>")
            msg.attach(msgImage)

            for i in range(len(self.receiver)):
                msg.attach(MIMEText(self.content.
                                    format(user=self.receiver_name[self.receiver.index(self.receiver[i])]),
                                    'html', 'utf-8'))

            # msg.attach(MIMEText(self.content.format(user=self.receiver_name), 'html', 'utf-8'))
            # return a
            # 邮件格式填写
                msg['from'] = Header(self.user_name, 'utf-8')
                msg['to'] = Header(self.receiver[i], 'utf-8')       # Header(";".join(self.receiver_name), 'utf-8')    # Header(self.receiver, 'utf-8')
            # msg['cc'] = Header('alexle@x2era.com', 'UTF-8')
                msg['subject'] = Header(self.subject, 'utf-8')
                return msg
        else:
            for i in range(len(self.receiver)):
                msg = MIMEText(self.content
                               .format(user=self.receiver_name[self.receiver.index(self.receiver[i])]),
                               'html', 'utf-8')
                msg['from'] = Header(self.mail_name, 'UTF-8')
                msg['to'] = ";".join(self.receiver)              # Header(self.receiver, 'utf-8')
            # msg['cc'] = Header('alexle@x2era.com', 'UTF-8')
                msg['subject'] = Header(self.subject, 'utf-8')
                return msg

    def send_mail(self):
        for i in range(len(self.receiver)):
            try:
                smtp = smtplib.SMTP()
                smtp.connect(self.mail_host)
                smtp.login(user=self.mail_name, password=self.mail_pass,)
            except:
                smtp = smtplib.SMTP_SSL()
                smtp.login(user=self.mail_name, password=self.mail_pass)
            aaa = self.mail_content()
            try:
                smtp.sendmail(self.mail_name, self.receiver[i], aaa.as_string())
                print("发送成功")
            except smtplib.SMTPException as e:
                print("发送失败", e)
            smtp.quit()


if __name__ == '__main__':
    a = SendEmail(
        mail_host='smtphz.qiye.163.com',
        port='25',
        mail_name='alexle@x2era.com',
        user_name='乐春霞',
        mail_pass='hhuE28EkeRXBms6S',
        receiver=['alexle@x2era.com',  '973166414@qq.com'],  # , 'yunqiuzhao@x2era.com'
        receiver_name=['乐春霞', '楽春霞'],
        subject='这是测试邮件的标题',
        content="""
                <p>Dear {user}:</p>
                <p style="text-indent:2em"> 这是测试邮件里面的内容,详情请点击链接或者下载附件。</p>
                <div> <a href = "https://www.baidu.com"><span font-size="20px">请点击这里</span></a></div>
                <p> 图片的演示：</p>
                <p> <img src="cid:image1" alt="本地文件的图片" width="300px"/></p>
                """,

        file='.\\picture.jpg'
    )
    a.send_mail()








