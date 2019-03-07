$(function () {
    $('.market').width(innerWidth)
    // console.log(111)

    $('.type-slider li').click(function () {
        $('.type-slider li').removeAttr('class')
        $(this).prop('class','active')
    })

})