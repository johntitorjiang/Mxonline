# _*_ coding:utf-8 _*_
__auther__ = 'Ginger'
__date__ = '2018/1/6 0006 10:58'
from django.core.mail import send_mail
from MxOnline.settings import EMAIL_FROM
from random import Random

from users.models import EmailVerifyRecord


# 生成随机验证码
def random_str(random_length=8):
    str = ''
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str


# 邮件发送函数
def send_register_email(email, send_type="register"):
    email_recode = EmailVerifyRecord()
    if send_type == "update_email":
        code = random_str(6)
    else:
        code = random_str(16)
    email_recode.code = code
    email_recode.email = email
    email_recode.send_type = send_type
    email_recode.save()

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "在线注册激活"
        email_body = "点击链接注册 http://47.93.26.147/active/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "重置密码链接"
        email_body = "点击链接重置密码 http://47.93.26.147/reset/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

        # 修改邮箱发送验证码
    elif send_type == "update_email":
        email_title = "邮箱修改验证码"
        email_body = "邮箱验证码为{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
