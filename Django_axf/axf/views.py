import hashlib
import random
import time
import os

from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from Django_axf import settings
from axf.VerifyCode import *
from axf.models import Wheel, Nav, Mustbuy, Shop, Mainshow, Foodtype, Goods, User, Cart, Order, OrderGoods


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

    #获取购物车信息
    token = request.session.get('token')
    userid = cache.get(token)
    if userid:
        user = User.objects.get(pk=userid)
        carts = user.cart_set.all()
        res['carts'] = carts


    return render(request,'market/market.html',context=res)


def cart(request):
    token = request.session.get('token')
    userid = cache.get(token)
    if userid:
        user = User.objects.get(pk=userid)
        carts = user.cart_set.filter(goodsnumber__gt=0)

        #默认情况下，购物车里面的东西都是全部选中状态，只要有一个不选中，全选就取消
        isall = True
        for cart in carts:
            if not cart.isselect:
                isall = False
        res = {'carts':carts,
               'isall':isall,
               }
        return render(request, 'cart/cart.html',context=res)
    else:
        return render(request,'cart/no-login.html')






def mine(request):
    # 获取
    token = request.session.get('token')
    userid = cache.get(token)
    user = None
    response_data = {}
    if userid:
        user = User.objects.get(pk=userid)
        response_data['user'] = user

        orders = user.order_set.all()
        #待支付
        response_data['waitpay'] = orders.filter(status = 0).count()
        #待收货
        response_data['paydone'] = orders.filter(status= 1).count()

    return render(request,'mine/mine.html',context=response_data)

#密码加密
def generate_password(res):
    md5 = hashlib.md5()
    md5.update(res.encode('utf-8'))
    return md5.hexdigest()
#token 唯一标识
def generate_token():
    temp = str(time.time()) + str(random.random())
    md5 = hashlib.md5()
    md5.update(temp.encode('utf-8'))
    return md5.hexdigest()





def register(request):

    if request.method == 'GET':
        # 登录时的验证码图片
        # vc = VerifyCode()
        # vc.generate()
        # print(vc.code)

        return render(request,'mine/register.html')
    elif request.method =='POST':

        email = request.POST.get('email')
        passowrd = generate_password(request.POST.get('password'))
        name = request.POST.get('name')
        # print(email,passowrd,name)

        #存入数据库
        user = User()
        user.email = email
        user.password = passowrd
        user.name = name
        user.save()

        #状态保持
        token = generate_token()
        #key-value >> token:userid
        cache.set(token,user.id,60*60*24*3)
        request.session['token'] = token

        return redirect('axf:mine')


# global vc_code

def login(request):
    if request.method == 'GET':
        # vc = VerifyCode()
        # vc.generate()
        # vc_code = vc

        return render(request,'mine/login.html')
    elif request.method =='POST':

        # login_code = request.POST.get('vc_code')
        # print(login_code)
        # if login_code==vc_code.code:

        email = request.POST.get('email')
        password = generate_password(request.POST.get('password'))
        print(email,password)

        #js中存入cookie中的参数来进行重定向
        back = request.COOKIES.get('back')
        print(back)

        user = User.objects.filter(email=email).filter(password=password)
        if user.exists():
            #状态保持
            user = user.first()
            token = generate_token()
            # key-value >> token:userid
            cache.set(token, user.id, 60 * 60 * 24 * 3)
            request.session['token'] = token
            if back == 'mine':
                return redirect('axf:mine')
            else:
                return redirect('axf:marketbase')
        else:
            return render(request,'mine/login.html',context={'err':'邮箱或密码有误！'})
        # else:
        #     return render(request, 'mine/login.html',context={'err1':'验证码有误！'})




def logout(request):
    request.session.flush()
    response = redirect('axf:mine')
    response.delete_cookie('base')

    return response




def upfile(request):
    # 判断是否为POST
    if request.method == 'POST':
        # 获取文件内容
        file = request.FILES['file']
        # 文件保存路径
        item = str(time.time()) + file.name
        filepath = os.path.join(settings.MDEIA_ROOT, item )
        with open(filepath, 'wb') as fp:
            for info in file.chunks():
                fp.write(info)
        # 文件写入
        token = request.session.get('token')
        userid = cache.get(token)
        user = User.objects.get(pk=userid)

        user.img = item
        user.save()

        return redirect('axf:mine')
    elif request.method == 'GET':

        return render(request,'mine/upfile.html')


def checkemail(request):
    res = request.GET.get('email')
    users = User.objects.filter(email=res)

    if users.exists():
        response_data = {
            'result':0,
            'msg':'用户名重复',
        }
        return JsonResponse(response_data)
    else:
        response_data = {
            'result': 1,
            'msg': '用户名可用',
        }
        return JsonResponse(response_data)


def addcart(request):
    token = request.session.get('token','')

    userid = cache.get(token)
    # print(userid) #获取登录用户信息userid

    if userid:  #true是已经登录状态
        user = User.objects.get(pk=userid)
        goodsid = request.GET.get('goodsid')
        # print('收到ajax数据产品id',goodsid)
        goods = Goods.objects.get(pk=goodsid)

        carts = Cart.objects.filter(user=user).filter(goods=goods)
        if carts.exists():
            cart = carts.first()
            cart.goodsnumber += 1
            cart.save()

        else:
            cart = Cart()
            cart.user = user
            cart.goods = goods
            cart.goodsnumber = 1
            cart.save()
        response_data = {
            'status': 1,
            'mig': '添加{}成功添加总数量{}'.format(cart.goods.productlongname, cart.goodsnumber),
            'goodsnumber':cart.goodsnumber
        }
        return JsonResponse(response_data)

    response_data = {
        'status':0,
        'msg':'请先进行登录'
    }
    return JsonResponse(response_data)


def subcart(request):
    #找到对应商品
    goodsid = request.GET.get('goodsid')
    # print(goodsid)
    goods = Goods.objects.get(pk=goodsid)

    #找到对应的用户
    token = request.session.get('token')
    userid = cache.get(token)
    user = User.objects.get(pk=userid)

    #获取对应的购物车信息
    cart = Cart.objects.filter(user=user).filter(goods=goods).first()
    cart.goodsnumber -= 1

    cart.save()

    respons_data = {
        'status':1,
        'msg':'商品从购物车移除',
        'goodsnumber':cart.goodsnumber
    }
    return JsonResponse(respons_data)

#改变购物车中要进行结算的选中状态
def changecartselect(request):
    cartid = request.GET.get('cartid')
    # print(cartid)
    cart = Cart.objects.get(pk=cartid)
    cart.isselect = not cart.isselect
    cart.save()

    response_data = {
        'status':1,
        'mssg':'选中状态修改完成',
        'isselect':cart.isselect
    }

    return JsonResponse(response_data)


def changecartall(request):
    isall = request.GET.get('isall')
    # print(isall)

    #获取用户
    token = request.session.get('token')
    userid = cache.get(token)
    user = User.objects.get(pk=userid)
    carts = user.cart_set.all()
    if isall == 'true':
        isall = True
    else:
        isall = False
    for cart in carts:
        cart.isselect = isall
        cart.save()

    response_data = {
        'status':1,
        'isall':isall,
        'msg':'全选状态已经改变',
    }
    return JsonResponse(response_data)

#生成订单方法
def generate_identifier():
    temp = str(int(time.time())) + str(random.randrange(1000,10000))
    return temp

#生成订单
def generateorder(request):
    #确定用户身份
    token = request.session.get('token')
    userid = cache.get(token)
    # print(userid)
    user = User.objects.get(pk=userid)
    # print(user)
    #生成订单
    order = Order()
    order.user = user #表明订单用户 属于谁
    order.identifier = generate_identifier() #生成订单号
    order.save()

    #订单中的商品 从购物车中循环拿出
    carts = user.cart_set.filter(isselect = True)

    for cart in carts:
        orderGoods = OrderGoods()
        orderGoods.order = order
        orderGoods.goods = cart.goods
        orderGoods.number = cart.goodsnumber
        orderGoods.save()
        #加入订单的商品从购物车中移除
        cart.delete()

    return render(request,'order/orderdetail.html',context={'order':order})



def orderlist(request):
    token = request.session.get('token')
    userid = cache.get(token)

    user = User.objects.get(pk=userid)

    #获取对应用户的订单 主获从
    orders= user.order_set.all()
    return render(request,'order/orderlist.html',context={'orders':orders})





def orderdetail(request,identifier):
    order = Order.objects.filter(identifier=identifier).first()

    return render(request,'order/orderdetail.html',context={'order':order})