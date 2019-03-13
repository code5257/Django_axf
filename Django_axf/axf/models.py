from django.db import models


#基础类
# insert into axf_wheel()
class BaseModel(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=10)

    class Meta:
        abstract = True

#轮播图
# insert into axf_wheel(img,name,trackid)
class Wheel(BaseModel):
    class Meta:
        db_table = 'axf_wheel'


#导航 模型类
class Nav(BaseModel):
    class Meta:
        db_table = 'axf_nav'


# 每日必购
class Mustbuy(BaseModel):
    class Meta:
        db_table = 'axf_mustbuy'

# 部分商品
class Shop(BaseModel):
    class Meta:
        db_table = 'axf_shop'


# 商品列表  模型类

class Mainshow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=100)

    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=10)
    productid1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=100)
    price1 = models.CharField(max_length=10)
    marketprice1 = models.CharField(max_length=10)

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=10)
    marketprice2 = models.CharField(max_length=10)

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=10)
    marketprice3 = models.CharField(max_length=10)

    class Meta:
        db_table = 'axf_mainshow'

class Foodtype(models.Model):
    #分类 ID
    typeid = models.CharField(max_length=10)
    #分类名称
    typename = models.CharField(max_length=100)
    #子类名称
    childtypenames = models.CharField(max_length=200)
    #排序
    typesort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtypes'



# insert into axf_goods(productid,productimg,productname,productlongname,isxf,pmdesc,specifics,price,marketprice,categoryid,childcid,childcidname,dealerid,storenums,productnum)
                # values("11951","http://img01.bqstatic.com/upload/goods/000/001/1951/0000011951_63930.jpg@200w_200h_90Q","","乐吧薯片鲜虾味50.0g",0,0,"50g",2.00,2.500000,103541,103543,"膨化食品","4858",200,4);
#商品 模型类
class Goods(models.Model):
    productid = models.CharField(max_length=100)
    productimg = models.CharField(max_length=100)
    productname = models.CharField(max_length=100)
    productlongname = models.CharField(max_length=100)
    isxf = models.IntegerField()
    pmdesc = models.IntegerField()
    specifics = models.CharField(max_length=100)
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(max_length=100)
    dealerid = models.CharField(max_length=100)
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'


class User(models.Model):
    # 邮箱
    email = models.CharField(max_length=40,unique=True)
    #密码
    password = models.CharField(max_length=256)
    #昵称
    name = models.CharField(max_length=100)
    #头像
    img = models.CharField(max_length=100,default='touxiang.jpg')
    #等级
    rank = models.IntegerField(default=1)

    class Meta:
        db_table ='axf_user'


#添加购物车模型类
#购物车是用户 对 商品 多对多模型 直接建立关系表
class Cart(models.Model):
    #用户 （添加商品到哪个用户）
    user = models.ForeignKey(User)

    #商品 （用户对应有哪些商品）
    goods = models.ForeignKey(Goods)

    #商品数量
    goodsnumber = models.IntegerField()

    # 是否选中
    isselect = models.BooleanField(default=True)
    # 是否删除
    isdelete = models.BooleanField(default=False)


    class Meta:
        db_table = 'axf_cart'

#订单 模型类
#一个用户 对应 多个订单
class Order(models.Model):
    #用户
    user = models.ForeignKey(User)
    #创建时间
    createtime = models.DateTimeField(auto_now_add=True)
    #更新时间
    updatetime = models.DateTimeField(auto_now=True)
    # 状态
    # -1 过期
    # 0 未付款
    # 1 已付款，待发货
    # 2 已发货，待收货
    # 3 已收货，待评价
    # 4 已评价
    status = models.IntegerField(default=0)
    # 订单号
    identifier = models.CharField(max_length=256)


class OrderGoods(models.Model):
    #订单
    order = models.ForeignKey(Order)
    #商品
    goods = models.ForeignKey(Goods)

    ##商品选择规格
    number = models.IntegerField()
