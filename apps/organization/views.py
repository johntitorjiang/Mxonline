# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import CourseOrg, CityDict, Teacher
from django.http import HttpResponse
from django.db.models import Q

from .forms import UserAskForm
from courses.models import Course
from operation.models import UserFavorite
# Create your views here.


# 课程机构列表
class OrgView(View):
    def get(self, request):
        # type: (object) -> object
        # 课程机构
        all_orgs = CourseOrg.objects.all()
        # 热门机构
        hot_orgs = all_orgs.order_by("-click_num")[:3]
        # 城市
        all_citys = CityDict.objects.all()
        # 搜索功能
        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_orgs = all_orgs.filter(Q(name__icontains=search_keywords) | Q(desc__icontains=search_keywords))
        # 筛选类别
        category = request.GET.get('ct', "")
        if category:
            all_orgs = all_orgs.filter(category=category)
        # 排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "student":
                all_orgs = all_orgs.order_by("-student")
            elif sort == "course_nums":
                all_orgs = all_orgs.order_by("-course_nums")
        # 筛选城市
        city_id = request.GET.get('city', "")
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))
        # 对课程机构分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 3, request=request)
        orgs = p.page(page)

        org_nums = all_orgs.count()
        return render(request, "org-list.html", {
            "all_orgs": orgs,
            "all_citys": all_citys,
            "org_num": org_nums,
            "city_id": city_id,
            "category": category,
            "hot_orgs": hot_orgs,
            "sort": sort
        })


# 用户咨询
class AddUserAskView(View):
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json')


# 机构首页
class OrgHomeView(View):
    def get(self, request, org_id):
        # type: (object, object) -> object
        current_page = "home"
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 点击数
        course_org.click_num += 1
        course_org.save()
        # 用户是否收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        # 利用外键取出model中的信息
        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all().order_by("-click_num")[:2]
        return render(request, 'org-detail-homepage.html', {
            'all_courses': all_courses,
            'all_teachers': all_teachers,
            'course_org': course_org,
            "current_page": current_page,
            "has_fav" : has_fav,
        })


# 机构课程列表页
class OrgCourseView(View):
    def get(self, request, org_id):
        # type: (object, object) -> object
        current_page = "course"
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 用户是否收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        # 利用外键取出model中的信息
        all_courses = course_org.course_set.all()
        return render(request, 'org-detail-course.html', {
            'all_courses': all_courses,
            'course_org': course_org,
            "current_page": current_page,
            "has_fav": has_fav,
        })


# 机构介绍页
class OrgDescView(View):
    def get(self, request, org_id):
        # type: (object, object) -> object
        current_page = "desc"
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 用户是否收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        return render(request, 'org-detail-desc.html', {
            'course_org': course_org,
            "current_page": current_page,
            "has_fav": has_fav,
        })


# 机构讲师页
class OrgTeacherView(View):
    def get(self, request, org_id):
        # type: (object, object) -> object
        current_page = "teacher"
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 用户是否收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        # 利用外键取出model中的信息
        all_teachers = course_org.teacher_set.all()
        return render(request, 'org-detail-teachers.html', {
            'all_teachers': all_teachers,
            'course_org': course_org,
            "current_page": current_page,
            "has_fav": has_fav,
        })


# 机构收藏及取消收藏
class AddFavView(View):
    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)

        if not request.user.is_authenticated():
            #判断用户登录状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

        exist_records = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        # 记录已存在，取消收藏
        if exist_records:
            exist_records.delete()

            if int(fav_type) == 1:
                course = Course.objects.get(id=int(fav_id))
                course.fav_num -= 1
                if course.fav_num < 0:
                    course.fav_num = 0
                    course.save()
            elif int(fav_type) == 2:
                course_org = CourseOrg.objects.get(id=int(fav_id))
                course_org.fav_num -= 1
                if course_org.fav_num < 0:
                    course_org.fav_num = 0
                    course_org.save()
            elif int(fav_type) == 3:
                teacher = Teacher.objects.get(id=int(fav_id))
                teacher.fav_num -= 1
                if teacher.fav_num < 0:
                    teacher.fav_num = 0
                    teacher.save()

            return HttpResponse('{"status":"success", "msg":"收藏"}', content_type='application/json')
        else:
            user_fav = UserFavorite()
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()

                if int(fav_type) == 1:
                    course = Course.objects.get(id=int(fav_id))
                    course.fav_num += 1
                    course.save()
                elif int(fav_type) == 2:
                    course_org = CourseOrg.objects.get(id=int(fav_id))
                    course_org.fav_num += 1
                    course_org.save()
                elif int(fav_type) == 3:
                    teacher = Teacher.objects.get(id=int(fav_id))
                    teacher.fav_num += 1
                    teacher.save()

                return HttpResponse('{"status":"success", "msg":"已收藏"}', content_type='application/json')

            else:
                return HttpResponse('{"status":"fail", "msg":"收藏出错"}', content_type='application/json')


# 教师列表信息
class TeacherListView(View):
    def get(self, request):
        all_teachers = Teacher.objects.all()
        hot_teachers = all_teachers.order_by("-click_num")[:5]
        # 搜索功能
        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_teachers = all_teachers.filter(Q(name__icontains=search_keywords) | Q(work_company__icontains=search_keywords) | Q(work_title__icontains=search_keywords))

        # 排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "hot":
                all_teachers = all_teachers.order_by("-fav_num")

        # 对教师机构分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_teachers, 5, request=request)
        teachers = p.page(page)

        return render(request, "teachers-list.html", {
            "all_teachers": teachers,
            "hot_teachers": hot_teachers,
            "sort": sort,

        })


# 讲师详情
class TeacherDetailView(View):
    def get(self, request, teacher_id):
        teacher = Teacher.objects.get(id=int(teacher_id))
        all_courses = Course.objects.filter(teacher=teacher)

        # 课程点击数
        teacher.click_num += 1
        teacher.save()

        has_teacher_faved = False

        if UserFavorite.objects.filter(user=request.user, fav_type=3, fav_id=teacher_id):
            has_teacher_faved = True

        has_org_faved = False
        if UserFavorite.objects.filter(user=request.user, fav_type=2, fav_id=teacher.org.id):
            has_org_faved = True

        # 讲师排行
        hot_teachers = Teacher.objects.all().order_by("-click_num")[:5]
        return render(request, "teacher-detail.html", {
            "hot_teachers": hot_teachers,
            "teacher": teacher,
            "all_courses": all_courses,
            "has_teacher_faved": has_teacher_faved,
            "has_org_faved": has_org_faved,
        })




