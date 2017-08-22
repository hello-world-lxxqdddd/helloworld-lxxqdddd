#_*_coding:utf-8

from .models import HomePage
import xadmin
from xadmin import views

class HomePageAdmin(object):
    list_display = ['banner_1','banner_1','banner_1','welcome_title','welcome_text1','welcome_text2','welcome_text3']


class GlobalSettings(object):
    site_title = "Hello-World后台管理系统"
    site_footer = "Hello-World: 龙先鹏"
    menu_style = 'according'


xadmin.site.register(HomePage,HomePageAdmin)
xadmin.site.register(views.CommAdminView,GlobalSettings)