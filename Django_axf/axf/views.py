from django.shortcuts import render

# Create your views here.
from axf.models import Wheel, Nav, Mustbuy, Shop, Mainshow, Foodtype, Goods


def home(request):
    wheel_list = Wheel.objects.all()
    nav_list = Nav.objects.all()
    mustbuy_list = Mustbuy.objects.all()
    shops = Shop.objects.all()
    mainshows = Mainshow.objects.all()

    shophead = shops[0]
    shoptaps = shops[1:3]
    shopclasss = shops[3:7]
    shopcommends = shops[7:11]

    res = {
        'wheel_list':wheel_list,
        'nav_list':nav_list,
        'mustbuy_list':mustbuy_list,
        'shophead':shophead,
        'shoptaps':shoptaps,
        'shopclasss':shopclasss,
        'shopcommends':shopcommends,
        'mainshows':mainshows,

    }

    return render(request,'home/home.html',context=res)


def market(request,childid='0',sortid='0'):
    foodtypes = Foodtype.objects.all()

    index = int(request.COOKIES.get('index','0'))
    categoryid = foodtypes[index].typeid

    if childid == '0':
        #为‘0’ 说明没有进行子类分类的操作显示一类中的全部商品
        goods_list = Goods.objects.filter(categoryid=categoryid)
    else:
        #获取某一类中的子类类型
        goods_list = Goods.objects.filter(categoryid=categoryid).filter(childcid=childid)

    # sortid = '0'时候默认综合排序，
    # 1销量排序 2价格最高 3价格最低
    if sortid == '1':
        goods_list = goods_list.order_by('-productnum')
    elif sortid =='2':
        goods_list = goods_list.order_by('-price')
    else:
        goods_list = goods_list.order_by('price')


    #获取子类的信息
    childtypenames = foodtypes[index].childtypenames
    #储存子类 信息
    childtype_list = []
    for item in childtypenames.split('#'):
        #有子类分类的情况下
        #item >> 子类名称：ID
        item_list = item.split(':')
        name = item_list[0]
        id = item_list[1]
        childdir = {
            'name':name,
            'id':id
        }
        childtype_list.append(childdir)

    res = {
        'foodtypes':foodtypes,
        'goods_list':goods_list,
        'childtype_list':childtype_list,
        'childid':childid,
    }

    return render(request,'market/market.html',context=res)


def cart(request):

    return render(request,'cart/cart.html')


def mine(request):

    return render(request,'mine/mine.html')