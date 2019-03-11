$(function () {
    $('.mine').width(innerWidth)
    // console.log(1)

    $('#login_ck').click(function () {

        $.cookie('back','mine',{expires:3,path:'/'})

        console.log(1111)
        window.open('/login/','_self')
    })


})