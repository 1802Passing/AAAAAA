# 系统（内置）模块

import xadmin  # 第三方模块
from xadmin import views

from art.models import Tag, Category, Art # 自定义模块

# 设置admin的站点样式
class BaseSettings:
    enable_themes = True
    use_bootswatch = True

class GlobalSettings:
    site_title = "创意小说"
    site_footer = '吃喝玩乐<h3></h3>'
    menu_style = 'accordion'
    global_search_models = [Tag]
    app_label_title = {
        'art' : '文章管理',   # 应用名：应用标题
    }
    app_icons = {
        'art' : 'gltphicon gltphicon-book'
    }




xadmin.site.register(views.BaseAdminView,BaseSettings)
xadmin.site.register(views.CommAdminView,GlobalSettings)

class TagAdmin:
    list_display = ('name','describe','add_time') # 展示字段
    list_per_page = 10  # 每页显示的记录数
    list_filter = ('add_time',) # 过滤字段-查询数据的条件
    search_fields = ('name','describe')  # 搜索字段

class CategoryAdmin:
    list_display = ('title','add_time')
    list_per_page = 10

class ArtAdmin:
    list_display = ('title','summary','author','category','tags')
    list_per_page = 10

xadmin.site.register(Tag,TagAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Art, ArtAdmin)

