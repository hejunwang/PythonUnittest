#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/2 0002 下午 10:24
# @Author  : toby
# @Site    :
# @File    : test3.py
# @Software: PyCharm


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os


def SendEmail():
    # 第三方 SMTP 服务
    mail_host = "smtp.126.com"  # 设置服务器
    mail_user = "mtbf_test_001"  # 用户名
    mail_pass = "qikutest123"  # 口令

    sender = "mtbf_test_001@126.com"
    receivers = ['287619892@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEMultipart("Mixed")
    message['From'] = sender
    message['To'] = ';'.join(receivers)

    #主题
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8').encode()      #邮件主题

    #文本内容
    text_plain = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    message.attach(text_plain)

    #文本2
    texthtml = 'https: // www.cnblogs.com / mpp0905 / p / 8419869.html'
    text2 =MIMEText(texthtml,'plain','utf-8')
    message.attach(text2)


    #  附件
    print("filepath --> {}".format(os.getcwd()))
    filepath = os.path.join(os.getcwd()+"\\"+"utils.py")
    print("filepath-->{}".format(filepath))
    sendfile = open(filepath,'rb').read()
    text_att = MIMEText(sendfile,'base64','utf-8')
    text_att["Content-Type"] = 'application/octet-stream'
    message.attach(text_att)


    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass) #登录邮箱
        smtpObj.sendmail(sender, receivers, message.as_string())
        print('SEND EMAIL OVER SUCCESS')
        smtpObj.quit()

    except smtplib.SMTPException as e:

        print("send error")
        print(e)



if __name__ == '__main__':
    SendEmail()

