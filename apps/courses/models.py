# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime
from DjangoUeditor.models import UEditorField

from django.db import models
from organization.models import CourseOrg, Teacher

# Create your models here.


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True)
    is_banner = models.BooleanField(default=False, verbose_name=u"广告轮播")
    name = models.CharField(max_length=50, verbose_name=u"课程名称")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    # Udeitor 富文本设置
    detail = UEditorField(verbose_name=u'课程详情', width=600, height=300, imagePath="course/Ueditor/image/",
                          filePath="course/Ueditor/files/", default='')
    degree = models.CharField(choices=(("prem", u"初级"), ("mid", u"中级"), ("high", u"高级")), max_length=5)
    learn_time = models.IntegerField(default=0, verbose_name=u"学习时长（分钟）")
    teacher = models.ForeignKey(Teacher, verbose_name=u"讲师", null=True, blank=True)
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_num = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="course/%Y/%m", default=u"image/default.png", max_length=100)
    click_num = models.IntegerField(default=0, verbose_name=u"点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    category = models.CharField(default=u"开发", max_length=30, verbose_name=u"课程描述")
    youneed_know = models.CharField(max_length=300, verbose_name=u"课程须知", default="")
    teacher_tell = models.CharField(max_length=300, verbose_name=u"老师告诉你", default="")
# 相同标签的课程会关联
    tag = models.CharField(default="", verbose_name=u"课程标签", max_length=20)

    class Meta:
        verbose_name = u"课程信息"
        verbose_name_plural = verbose_name

    # 获取章节数
    def get_zj_num(self):
        return self.lesson_set.all().count()
    # 函数在后台显示的名称
    get_zj_num.short_description = "章节数"

    # 学习用户
    def get_learn_user(self):
        return self.usercourse_set.all()[:5]

    # 课程章节
    def get_course_lesson(self):
        return self.lesson_set.all()

    # 被引用外键重载,在后台保存和删除是会显示名称，否则显示xxxxx object
    def __unicode__(self):
        return self.name


# 将表中特殊项筛选出来单独管理
class BannerCouse(Course):
    class Meta:
        verbose_name = "轮播课程"
        verbose_name_plural = verbose_name
        proxy = True


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"章节名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节信息"
        verbose_name_plural = verbose_name

     # 课程章节视频
    def get_lesson_video(self):
        return self.video_set.all()

    # 被引用外键重载
    def __unicode__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节")
    name = models.CharField(max_length=100, verbose_name=u"视频名称")
    url = models.CharField(max_length=200, default="", verbose_name=u"访问链接")
    learn_time = models.IntegerField(default=0, verbose_name=u"学习时长（分钟）")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    # 被引用外键重载
    def __unicode__(self):
        return self.name

class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程1")
    name = models.CharField(max_length=100, verbose_name=u"资源名称")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"资源文件", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"资源"
        verbose_name_plural = verbose_name

    # 被引用外键重载
    def __unicode__(self):
        return self.name
