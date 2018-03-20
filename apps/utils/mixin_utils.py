# _*_ coding:utf-8 _*_
__auther__ = 'Ginger'
__date__ = '2018/1/28 0028 22:38'

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# 登陆验证View
class LoginRequiredMixin(object):

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)