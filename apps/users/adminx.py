# _*_ coding:utf-8 _*_
__auther__ = 'Ginger'
__date__ = '2017/12/28 15:06'

# 注册admin
import xadmin
from xadmin import views

from .models import EmailVerifyRecord
from .models import Banner, UserProfile


# 主题
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


# 顶部和底部名称
class GlobalSetting(object):
    site_title = u"后台管理"
    site_footer = u"大力智慧教育"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    # 定义显示项及顺序
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索功能
    search_fields = ['code', 'email', 'send_type',]
    # 筛选字段
    list_filter = ['email', 'send_type', 'send_time']
    # icon
    model_icon = 'fa fa-code'


class BannerAdmin(object):
    # 定义显示项及顺序
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    # 搜索功能
    search_fields = ['title', 'image', 'url', 'index']
    # 筛选字段
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
# 注册
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
