"""nova URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.conf.global_settings import MEDIA_ROOT
from django.conf.urls import url, include
from django.views.static import serve
from xadmin.views.website import IndexView

from apps.users.views.activeUserView import ActiveUserView
from apps.users.views.forgetPwdView import ForgetPwdView
from apps.users.views.loginView import LoginView
from apps.users.views.logoutView import LogoutView
from apps.users.views.modifyPwdView import ModifyPwdView
from apps.users.views.registerView import RegisterView
from apps.users.views.resetView import ResetView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    # 配置页面
    url('^$', IndexView.as_view(), name="index"),
    url('^login/$', LoginView.as_view(), name="login"),
    url('^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),

    # 验证用户注册后，在邮件里点击注册链接
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
    url(r'^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),

    # 退出登录
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    # 课程机构URL配置
    url(r'^org/', include('organization.urls', namespace="org")),

    # 课程相关URL配置
    url(r'^course/', include('courses.urls', namespace="course")),

    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

    # url(r'^static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}),

    # 课程相关URL配置
    url(r'^users/', include('users.urls', namespace="users")),

]


# 全局 404 页面配置（django 会自动调用这个变量）
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'