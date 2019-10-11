import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.config import *

def send_email(report_file):
    msg = MIMEMultipart()
    msg.attach(MIMEText(open(report_file,encoding='utf-8').read(),'html','utf-8')) # 添加html格式邮件正文（会丢失css格式）
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = Header(subject,charset='utf-8')

    att1 = MIMEText(open(report_file,'rb').read(),'base64','utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    att1['Content-Disposition'] = 'attachment;filename="report.html"'
    msg.attach(att1)

    try:
        smtp = smtplib.SMTP_SSL(smtp_server)
        smtp.login(smtp_user,smtp_password)
        smtp.sendmail(sender,receiver,msg.as_string())
        logging.info('发送成功')
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()

