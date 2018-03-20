# _*_ coding:utf-8 _*_
__auther__ = 'Ginger'
__date__ = '2017/12/28 16:33'

import xadmin

from .models import Course, Lesson, Video, CourseResource, BannerCouse
from organization.models import CourseOrg


# 在课程中嵌套修改章节信息，但是不能二层嵌套
class LessonInLine(object):
    model = Lesson
    extra = 0


# 在章节中嵌套修改视频信息，但是不能二层嵌套
class VideoInLine(object):
    model = Video
    extra = 0


# 在章节中嵌套修改视频信息，但是不能二层嵌套
class CourseResourceInLine(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    # 显示model中函数返回的数据,不保存在数据库'get_zj_num'
    list_display = ['name', 'course_org', 'desc', 'degree', 'learn_time', 'students', 'fav_num', 'click_num', 'is_banner', 'add_time', 'get_zj_num']
    search_fields = ['name', 'course_org', 'desc', 'detail', 'degree', 'learn_time', 'students', 'is_banner']
    list_filter = ['name', 'course_org', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_num', 'image', 'click_num', 'is_banner', 'add_time']
    # 默认排列
    ordering = ['-click_num']
    # 只读字段
    readonly_fields = ['click_num', 'fav_num', 'students']
    # 隐藏字段，和只读互斥
    exclude = []
    # 在课程中嵌套修改章节信息
    inlines = [LessonInLine, CourseResourceInLine]
    # 在列表页上直接修改内容
    list_editable = ['degree', 'desc']
    # 富文本
    style_fields = {"detail": "ueditor"}
    # excel文件导入
    import_excell= True
    # # 刷新
    # refresh_times = [3]

    # 筛选课程是否设置轮播
    #def queryset(self):
    #    qs = super(CourseAdmin, self).queryset()
    #    qs = qs.filter(is_banner=False)
    #    return qs

    # 在保存课程时统计课程机构课程数
    def save_models(self):
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()

    # excel文件导入
    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(CourseAdmin, self).post(request, args, kwargs)


class BannerCourseAdmin(object):
    list_display = ['name', 'course_org', 'desc',  'degree', 'learn_time', 'students', 'fav_num', 'click_num', 'add_time']
    search_fields = ['name', 'course_org', 'desc', 'detail', 'degree', 'learn_time', 'students']
    list_filter = ['name', 'course_org', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_num', 'image', 'click_num', 'add_time']
    # 默认排列
    ordering = ['-click_num']
    # 只读字段
    readonly_fields = ['click_num', 'fav_num']
    # 隐藏字段，和只读互斥
    exclude = []
    # 在课程中嵌套修改章节信息
    inlines = [LessonInLine, CourseResourceInLine]
    style_fields = {"detail":"ueditor"}

    # 筛选过滤
    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


class LessonAdmin(object):
    list_display = ['name',  'course', 'add_time']
    search_fields = ['name',  'course']
    list_filter = ['name',  'course__name', 'add_time']
    # 在课程中嵌套修改章节信息
    inlines = [VideoInLine]


class VideoAdmin(object):
    list_display = ['name', 'lesson', 'add_time']
    search_fields = ['name', 'lesson']
    list_filter = ['name', 'lesson', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['name', 'course', 'download', 'add_time']
    search_fields = ['name', 'course', 'download']
    list_filter = ['name', 'course', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(BannerCouse, BannerCourseAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
