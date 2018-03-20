# _*_ coding:utf-8 _*_


import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc',  'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'fav_num', 'click_num', 'image', 'city', 'address']
    search_fields = ['name', 'fav_num', 'image', 'city','']
    list_filter = ['name', 'fav_num', 'click_num', 'image', 'city', 'address']
    # 增加搜索功能
    relfield_style = 'fk_ajax'

class TeacherAdmin(object):
    list_display = ['name', 'org', 'add_time', 'work_year', 'work_company', 'work_title', 'point', 'fav_num', 'click_num']
    search_fields = ['name', 'org', 'work_year', 'work_company', 'work_title', 'point', 'fav_num', 'click_num']
    list_filter = ['name', 'org', 'add_time', 'work_year', 'work_company', 'work_title', 'point', 'fav_num', 'click_num']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
