var $item = $('.carousel-item'); 
var $wHeight = $(window).height();
$item.eq(0).addClass('active');
$item.height($wHeight); 
$item.addClass('full-screen');

$('.carousel img').each(function() {
  var $src = $(this).attr('src');
  var $color = $(this).attr('data-color');
  $(this).parent().css({
    'background-image' : 'url(' + $src + ')',
    'background-color' : $color,
    // 'background-size' : 'contain'
  });
  $(this).remove();
});

$(window).on('resize', function (){
  $wHeight = $(window).height();
  $item.height($wHeight);
});

$('.carousel').carousel({
  interval: 6000,
  pause: "false"
});

$(document).ready(function() {
    var users_box = $('.reserve-author-profile-img')
    console.log(users_box);
    function generateRandomColors(){
        var clr_1 = Math.floor(Math.random()*256);
        var clr_2 = Math.floor(Math.random()*256);
        var clr_3 = Math.floor(Math.random()*256);

        return `rgb(${clr_1},${clr_2},${clr_3})`;
    }

    for (var i=0; i<users_box.length; i++){
        $(users_box[i]).css('background-color',`${generateRandomColors()}`)
    }
 
  $('.admin-menu-btn').click(function(){
    $('.menu-box-in').stop().animate({
        width : 'toggle'
    },500);
  });
  
  $('.admin-menu-btn').click(function(){
    $('.menu-box-left').css("display","block");
    $('body').css("overflow","hidden");
  });
  $('.menu-box-left').click(function(){
    $('.menu-box-left').css("display","none");
    $('.menu-box-in').stop().animate({
        width : 'toggle'
    },500);
    $('body').css("overflow","auto");
  });

  $("#custom-carousel").owlCarousel({
      loop: true,
      nav: false,
      dots : false,
      autoPlay: 3000, //Set AutoPlay to 3 seconds
 
      responsive: {
        1: {
            items: 1,
        },
        500: {
          items: 2
        },
        600: {
            items: 2
        },
        800: {
            items: 3
        },
        1000: {
            items: 4
        }
      },
      itemsDesktop : [1199,3],
      itemsDesktopSmall : [979,3]
 
  });

  $("#custom-retaurant-carousel").owlCarousel({
    loop: true,
    nav: true,
    dots : false,
    autoPlay: 3000, //Set AutoPlay to 3 seconds

    responsive: {
      1: {
          items: 2,
      },
      600: {
          items: 3
      },
      800: {
          items: 4
      },
      1000: {
          items: 5
      }
    },
    itemsDesktop : [1199,3],
    itemsDesktopSmall : [979,3]

});
 
});


$(document).mouseup(function (e) { 
  console.log($(e.target).closest(".custom-drop-down").length);
      if ($(e.target).closest(".custom-drop-down").length === 0) { 
          $(".custom-drop-down").hide(); 
      } 
  }); 
  $('.header-btn').click(function(){
      $('.custom-drop-down').hide()
      $(this).siblings('.custom-drop-down').toggle()
  });