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
    $('.glyphicon-minus').hide()
    $('.bt-wrapper>i').hide()

    $('.bt-wrapper>.glyphicon-plus').click(function () {
        // console.log(1)
        //哪件产品，通过属性来确认
        request_data = {
            'goodsid':$(this).attr('data-goodsid')
        }
        $.get('/addcart/',request_data,function (response) {
            if(!response.status){
                console.log('请登录')
                //用cookie传参数 用于登陆后回到market界面，ajax中不能重定向
                $.cookie('back','market',{expires: 3,path: '/'})
                window.open('/login/','_self')
            }else{
                console.log('已经登录')
            }

        })

    })


})