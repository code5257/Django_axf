$(function () {
    $('.cart').width(innerWidth)

    money()

    //为购物车每个商品前面加点击事件，并进行选中和不选中的样式显示处理
    $('.cart .confirm-wrapper').click(function () {
        //控制选中状态的标签为$（this）下的span
        $span = $(this).find('span')

        request_data = {
            'cartid':$(this).attr('data-cartid')
        }

        $.get('/changecartselect/',request_data,function (response) {
            console.log(response)
            if (response.status == 1){
                if (response.isselect){
                    $span.removeClass('no').addClass('glyphicon glyphicon-ok')
                }else{
                    $span.removeClass('glyphicon glyphicon-ok').addClass('no')
                }
                money()
            }
        })
    })

    //结算界面的全选和取消全选的状态显示处理，一开始默认全选
    $('.bill-left .all').click(function () {
        $span = $(this).find('span')
        var isall = $(this).attr('isall')

        isall = (isall==  'false' )? true:false

        //点击后 先把全选样式改变 并把自定义属性改掉（自定义属性为ture代表全选）
        $(this).attr('isall',isall)
        if (isall){
                $span.removeClass('no').addClass('glyphicon glyphicon-ok')
        }else{
                $span.removeClass('glyphicon glyphicon-ok').addClass('no')

        }

        request_data = {
            'isall':$(this).attr('isall')
        }

        // 把全选是否选中状态发给服务端 ，
        $.get('/changecartall/',request_data,function (response) {
            console.log(response)
            if (response.status == 1){
                $('.confirm-wrapper').each(function () {
                    if (isall){
                        $(this).find('span').removeClass('no').addClass('glyphicon glyphicon-ok')
                    }else{
                        $(this).find('span').removeClass('glyphicon glyphicon-ok').addClass('no')
                    }
                    money()
                })
            }
        })
    })


    //下单价格计算
    function money(){
        var sum = 0

        // 遍历 获取 选中
        $('.cart li').each(function () {
            var $confirm = $(this).find('.confirm-wrapper')
            var $content = $(this).find('.content-wrapper')

            // 选中状态
            if ($confirm.find('.glyphicon').length){
                var price = $content.find('.price').attr('price')
                var num = $content.find('.num').attr('goodsnumber')

                sum += num * price
            }
        })
        console.log(sum)
        // 显示
        $('.bill .total b').html(sum)
    }

})