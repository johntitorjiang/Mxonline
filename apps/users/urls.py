# _*_ coding:utf-8 _*_
__auther__ = 'Ginger'
__date__ = '2018/1/30 0030 23:29'
from django.conf.urls import url, include

from users.views import UserInfoView, UoloadImageView, UpdatePwdView, SendEmailCodeView, UpdateUserEmailView\
    , MycourseView, MyfavOrgView,MyfavTeacherView, MyfavCourseView, MyMessageView


urlpatterns = [
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name="user_info"),
    # 用户头像修改
    url(r'^image/upload/$', UoloadImageView.as_view(), name="image_upload"),
    # 用户个人中心修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),
    # 用户个人中心修改邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),
    # 修改邮箱
    url(r'^update_email/$', UpdateUserEmailView.as_view(), name="update_email"),
    # 用户课程
    url(r'^my_course/$', MycourseView.as_view(), name="my_course"),
    # 我的收藏-课程机构
    url(r'^myfav/org/$', MyfavOrgView.as_view(), name="myfav_org"),
    # 我的收藏-机构讲师
    url(r'^myfav/teacher/$', MyfavTeacherView.as_view(), name="myfav_teacher"),
    # 我的收藏-课程
    url(r'^myfav/course/$', MyfavCourseView.as_view(), name="myfav_course"),
    # 我的消息
    url(r'^mymessage/$', MyMessageView.as_view(), name="mymessage"),


]