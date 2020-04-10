from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage
import smtplib


mail_host = 'smtphz.qiye.163.com'
mail_name = 'alexle@x2era.com'  # lechunxiaing@163.com
mail_pass = 'hhuE28EkeRXBms6S'  # 网易：PJVFOXNUTFAEBLBN   GLSAJVDERCGPLNPO   QQ：rptkvjpzuonmbbib

sender = 'alexle@x2era.com'
reciver = ['alexle@x2era.com',  'yunqiuzhao@x2era.com']   #  'yunqiuzhao@x2era.com'
# cc_reciver = 'alexle@x2era.com'
reciver_name = ['乐春霞', '云秋']   # '云秋'

content = """
<p>Dear {}:</p>
    <p style="text-indent:2em"> 这是测试邮件里面的内容,详情请点击链接或者下载附件。</p>
    <div> <a href = "https://www.baidu.com"><span font-size="20px">请点击这里</span></a></div>
    <p> 图片的演示：</p>
    <p> <img src="cid:image1" alt="本地文件的图片" width="300px"/></p>
    
"""
for i in range(len(reciver)):
    msg = MIMEMultipart('related')

    msg['from'] = Header('alexle@x2era.com', 'UTF-8')
    msg['to'] = Header(reciver[i], 'utf-8')
    # msg['cc'] = Header('alexle@x2era.com', 'UTF-8')
    subject = '这是测试邮件的标题'
    msg['subject'] = Header(subject, 'utf-8')

    msg2 = MIMEMultipart('alternative')
    msg.attach(msg2)
    # 添加图片
    msg2.attach(MIMEText(content.format(reciver_name[reciver.index(reciver[i])]), 'html', 'utf-8'))
    msgImag = MIMEImage(open('picture.jpg', 'rb').read())
    msgImag.add_header('Content-ID', '<image1>')
    msg.attach(msgImag)

    # 添加附件
    att1 = MIMEText(open('newV_punch.py', 'rb').read(), 'base64', 'utf-8')
    att1['content-type'] = 'application/octet-stream'
    att1['content-disposition'] = 'attachment; filename = "newV_punch.py"'
    msg2.attach(att1)
    try:
        smtp = smtplib.SMTP()
        smtp.connect(mail_host, 25)
        smtp.login(mail_name, mail_pass)
        smtp.sendmail(sender, reciver, msg.as_string())

    except smtplib.SMTPException as e:
        print('邮件发送失败')
        print(e)


