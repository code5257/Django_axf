from django.conf.urls import url

from axf import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^home/$',views.home,name='home'),

    url(r'^market/$',views.market,name='marketbase'),
    url(r'^market/(?P<childid>\d+)/(?P<sortid>\d+)/$',views.market,name='market'),

    url(r'^cart/$',views.cart,name='cart'),

    url(r'^mine/$',views.mine,name='mine'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^checkemail/$',views.checkemail,name='checkemail'),#ajax请求 数据交互
    url(r'^upfile/$',views.upfile,name='upfile'),#换头像

    url(r'^addcart/$',views.addcart,name='addcart'),
    url(r'^subcart/$',views.subcart,name='subcart'),
    #ajax 请求
    url(r'^changecartselect/$',views.changecartselect,name='changecartselect'),
    url(r'^changecartall/$',views.changecartall,name='changecartall'),

]