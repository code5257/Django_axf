$(function () {
        //恢复盒子大小
        $('.home').width(innerWidth)

        var swiper = new Swiper('#topSwiper', {
                pagination: '.swiper-pagination',
                nextButton: '.swiper-button-next',
                prevButton: '.swiper-button-prev',
                slidesPerView: 1,
                paginationClickable: true,
                spaceBetween: 30,
                loop: true,
                autoplay:2500,
            });

        var mustbuyswiper = new Swiper('#mustbuySwiper', {
                slidesPerView: 3,
                paginationClickable: true,
                spaceBetween: 5,
                loop: true,
            });
})

