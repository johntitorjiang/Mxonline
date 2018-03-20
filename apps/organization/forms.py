# _*_ coding:utf-8 _*_
__auther__ = 'Ginger'
__date__ = '2018/1/13 0013 16:24'
import re
from django import forms

from operation.models import UserAsk


class UserAskForm(forms.ModelForm):

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course']

    # 表单手机号码验证
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        # 正则表达式验证手机号码
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法", code="mobile_invalid")