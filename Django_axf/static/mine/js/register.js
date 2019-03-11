$(function () {
    $('.register').width(innerWidth)
    // console.log(1)

    var email_reg = /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/;
    $('#email .form-control').blur(function () {
        //表单失去焦点后操作
        if (!email_reg.test($(this).val())) {
            $('#email').removeClass('has-success').addClass('has-error')
            $('#email span').eq(1).removeClass().addClass('glyphicon glyphicon-remove form-control-feedback')
            $('#email input').attr('data-content', '邮箱格式错误').popover('show')

        } else {
            // 账号是否可用 [必须发给服务器]
            // 只需要 服务器 提示 可用true/不可用false
            // 通过ajax和服务器通信

            // jQuery.get( url [, data ] [, success(data, textStatus, jqXHR) ] [, dataType ] )
            // jQuery.post( url [, data ] [, success(data, textStatus, jqXHR) ] [, dataType ] )
            // jQuery.getJSON( url [, data ] [, success(data, textStatus, jqXHR) ] )
            request_data = {
                'email':$(this).val(),
            }
            $.get('/checkemail/',request_data,function (response) {
                //回调函数，客户端接收到服务器响应参数 response 做出的处理
                console.log(response)
                if(response.result){
                    $('#email').removeClass('has-error').addClass('has-success')
                    $('#email span').eq(1).removeClass().addClass('glyphicon glyphicon-ok form-control-feedback')
                    $('#email input').attr('data-content',response.msg).popover('hide')
                }else{
                    $('#email').removeClass('has-success').addClass('has-error')
                    $('#email span').eq(1).removeClass().addClass('glyphicon glyphicon-remove form-control-feedback')
                    $('#email input').attr('data-content',response.msg).popover('show')
                }
            })


            }

    })

    var password_reg = /^[a-zA-Z0-9]{6,12}$/;
    $('#password .form-control').blur(function () {
        //表单失去焦点后操作
        if (!password_reg.test($(this).val())) {
            $('#password').removeClass('has-success').addClass('has-error')
            $('#password span').eq(1).removeClass().addClass('glyphicon glyphicon-remove form-control-feedback')
            $('#password input').attr('data-content', '密码长度错误').popover('show')

        } else {
            $('#password').removeClass('has-error').addClass('has-success')
            $('#password span').eq(1).removeClass().addClass('glyphicon glyphicon-ok form-control-feedback')
            $('#password input').attr('data-content','格式正确').popover('hide')
        }

    })

    $('#name .form-control').blur(function () {
        //表单失去焦点后操作
        if ($(this).val().length > 2 && $(this).val().length < 12) {
            $('#name').removeClass('has-error').addClass('has-success')
            $('#name span').eq(1).removeClass().addClass('glyphicon glyphicon-ok form-control-feedback')
            $('#name input').attr('data-content','格式正确').popover('hide')

        } else {
            console.log($(this).val().length)
            $('#name').removeClass('has-success').addClass('has-error')
            $('#name span').eq(1).removeClass().addClass('glyphicon glyphicon-remove form-control-feedback')
            $('#name input').attr('data-content','昵称格式错误').popover('show')
        }

    })

    // $('#verifycode .form-control').blur(function () {
    //     //表单失去焦点后操作
    //     if(!reg.test($(this).val())){
    //         $('#email span').eq(1).removeClass().addClass('glyphicon glyphicon-remove form-control-feedback')
    //         $('#email input').attr('data-content','邮箱格式错误').popover('show')
    //
    //     }else {
    //         $('#email span').eq(1).removeClass().addClass('glyphicon glyphicon-ok form-control-feedback')
    //     }
    //
    // })


    //为按钮添加点击时间，且判断是否要提交form表单
    $('.register button').click(function () {
        var bo = 0

        $('.input-group').each(function () {
            if($(this).is('.has-success')) {
                $('.register form').submit()
            }
        })

    })






})
