# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"城市")
    desc = models.CharField(max_length=200, verbose_name=u"描述")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"城市信息"
        verbose_name_plural = verbose_name

    # 被引用外键重载
    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"机构名称")
    desc = models.TextField(verbose_name=u"机构描述")
    category = models.CharField(verbose_name=u"机构类别", default="orgs", max_length=20,
                                choices=(("orgs", "培训机构"), ("humans", "个人"), ("university", "高校")))
    fav_num = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name=u"org_logo",
                              default=u"image/default.png", max_length=100)
    click_num = models.IntegerField(default=0, verbose_name=u"点击数")
    city = models.ForeignKey(CityDict, verbose_name=u"所在城市")
    address = models.CharField(max_length=150, verbose_name=u"机构地址")
    student = models.IntegerField(default=0, verbose_name=u"学习人数")
    course_nums = models.IntegerField(default=0, verbose_name=u"课程数")
    add_time = models.DateTimeField(default=datetime.now)
    tag = models.CharField(max_length=100, verbose_name=u"机构标签", default=u"智慧牛逼")

    class Meta:
        verbose_name = u"机构信息"
        verbose_name_plural = verbose_name

    # 获取课程机构教师数
    def get_teacher_num(self):
        return self.teacher_set.all().count()

    # 被引用外键重载
    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u"所属机构")
    name = models.CharField(max_length=50, verbose_name=u"教师名称")
    work_year = models.IntegerField(default=0, verbose_name=u"工作年限")
    work_company = models.CharField(max_length=50, verbose_name=u"就职公司")
    work_title = models.CharField(max_length=50, verbose_name=u"公司职位")
    point = models.CharField(max_length=50, verbose_name=u"教学特点")
    click_num = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_num = models.IntegerField(default=0, verbose_name=u"收藏人数")
    age = models.IntegerField(default=18, verbose_name=u"年龄")
    image = models.ImageField(upload_to="teacher/%Y/%m", verbose_name=u"教师头像", default="", max_length=100)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name

    # 被引用外键重载
    def __unicode__(self):
        return self.name

    # 课程数
    def get_course_num(self):
        return self.course_set.all().count()
