from django.shortcuts import render

# Create your views here.
from axf.models import Wheel, Nav, Mustbuy, Shop, Mainshow, Foodtype


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


def market(request):
    foodtypes = Foodtype.objects.all()

    res = {
        'foodtypes':foodtypes,
    }

    return render(request,'market/market.html',context=res)


def cart(request):

    return render(request,'cart/cart.html')


def mine(request):

    return render(request,'mine/mine.html')