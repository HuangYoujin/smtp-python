#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import simplejson as json
import os
import sys

mail_host = 'smtp.gmail.com'
mail_subject = ''
mail_from = ''
mail_user = ''
mail_pw = ''
mail_content = ''
# mail_host = 'smtp.qq.com'
# mail_user = raw_input('请输入登录的邮箱:')
# mail_pw = raw_input('请输入您的密码:')

current = sys.path[0]

if hasattr(sys,'frozen'):
   current = os.path.dirname(sys.executable)

def readFile(fileName):
   object = open(fileName,'r')
   content = object.read();
   print 'Content:'+ content
   reload(sys)
   sys.setdefaultencoding('utf8')
   encodeObj = json.loads(str(content))

   global mail_subject,mail_from,mail_user,mail_pw,mail_content

   mail_subject = encodeObj[unicode("主题")]
   mail_from = encodeObj[unicode("来自")]
   mail_user = encodeObj[unicode("邮箱")]
   mail_content = encodeObj[unicode("内容")]
   mail_pw = raw_input('请输入您的密码:')

   print 'encodeObj:+++++++++'+encodeObj[unicode("邮箱")]
   object.close()

readFile(current+'/content.txt')

sender = 'xxxxxxxxx'
receivers = ['3530584119@qq.com']

# message = MIMEText(mail_content,'html','gb2312')
message = MIMEText(mail_content,'plain','utf-8')
message['From'] = Header(mail_from,'utf-8')
message['To'] = Header("美女Mika",'utf-8')
message['Subject'] = Header(mail_subject,'utf-8')

try:
   print "正在发送邮件,请勿关闭..."
   smtpObj = smtplib.SMTP()
   smtpObj.set_debuglevel(False)
   smtpObj.connect(mail_host,587)
   smtpObj.ehlo()
   smtpObj.starttls()
   smtpObj.ehlo()
   smtpObj.login(mail_user,mail_pw)
   smtpObj.sendmail(sender, receivers, message.as_string())     
   print "成功发送邮件! Bingo!!"
except Exception, e:
   print "发送邮件失败了..."

