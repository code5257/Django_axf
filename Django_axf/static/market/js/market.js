$(function () {
    $('.market').width(innerWidth)

    //用jquery.cookie
    var index = $.cookie('index')
    // console.log(index)
    if (index) {
        $('.type-slider li').eq(index).addClass('active')
    } else {
        $('.type-slider li:first').addClass('active')
    }
    $('.type-slider li').click(function () {
        // console.log(11)
        $.cookie('index', $(this).index(), {expires: 3, path: '/'})
    })


    var categoryShow = false
    $('#category-bt').click(function () {
        console.log(categoryShow)
        categoryShow = !categoryShow

        categoryShow ? categoryViewShow() : categoryViewHide()

    })

//分类蒙层显示
    function categoryViewShow() {
        $('.category-view').show()
        categoryShow = true
        sortViewHide()
        $('#category-bt i').removeClass().addClass('glyphicon glyphicon-chevron-down')
    }

    //分类蒙层隐藏
    function categoryViewHide() {
        $('.category-view').hide()
        categoryShow = false
        $('#category-bt i').removeClass().addClass('glyphicon glyphicon-chevron-up')

    }


    var sortShow = false
    $('#sort-bt').click(function () {
        sortShow = !sortShow
        sortShow ? sortViewShow() : sortViewHide()

    })

    //排序蒙层显示
    function sortViewShow() {
        $('.sort-view').show()
        sortShow = true
        categoryViewHide()
        $('#sort-bt i').removeClass().addClass('glyphicon glyphicon-chevron-down')

    }

    //排序蒙层隐藏
    function sortViewHide() {
        $('.sort-view').hide()
        sortShow = false
        $('#sort-bt i').removeClass().addClass('glyphicon glyphicon-chevron-up')

    }




///////////////////////////////////////////////////
//商品没有添加购物车时 减号和数量都不显示
//     $('.glyphicon-minus').hide()
//     $('.bt-wrapper>i').hide()
    //当数量大于零的时候就不隐藏，所以进行判断
    $('.bt-wrapper .num').each(function () {
        var num = parseInt($(this).html())
        if (num){
            $(this).show()
            $(this).prev().show()
        }else{
            $(this).hide()
            $(this).prev().hide()
        }
    })



    $('.bt-wrapper>.glyphicon-plus').click(function () {
        var $that = $(this)
        // console.log(1)
        //哪件产品，通过属性来确认
        request_data = {
            'goodsid':$(this).attr('data-goodsid')
        }
        $.get('/addcart/',request_data,function (response) {
            if(response.status == 0){
                console.log('请登录')
                //用cookie传参数 用于登陆后回到market界面，ajax中不能重定向
                $.cookie('back','market',{expires: 3,path: '/'})
                window.open('/login/','_self')
            }else if(response.status == 1){
                // console.log('已经登录')
                console.log(response)
                // 有问题，改变的是所有
                // $('.bt-wrapper .num').html(response.number)

                // 用兄弟节点 [操作按钮 this]
                // this 谁调用 指向 谁
                // 当前函数是ajax触发的 ，所以 $(this) 指向 ajax
                // $(this).prev().html(response.number)
                $that.prev().html(response.goodsnumber)

                //加号 的前一个和前两个兄弟 数量 和 减号都显示出来

                $that.prev().show()
                $that.prev().prev().show()
            }

        })

    })

    $('.bt-wrapper .glyphicon-minus').click(function () {
        var $that = $(this)
        request_data = {
            'goodsid': $(this).attr('data-goodsid')
        }

        $.get('/subcart/',request_data,function (response) {
            console.log(response)
            if(response.status == 1){
                if(response.goodsnumber){
                    $that.next().html(response.goodsnumber)
                }else{
                    $that.hide()
                    $that.next().hide()
                }
            }
        })

    })

})