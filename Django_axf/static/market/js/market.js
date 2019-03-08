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

})