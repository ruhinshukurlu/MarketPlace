count = 0
total_price = 0
$('.total-price').text(total_price)

$('.menu-items-style').click(function(){
    $('.total-price-box').css('display','flex')
    count += 1
    
    $('#complete-box-form').css('display', 'block')
    $('.choosen-items-container').css('display', 'flex')
    $(this).addClass(`item${count}`)
    if($(this).data('clicked'))
    {
        
        $(this).css('border', '1px solid #ccc')
        $(this).siblings('.menu-item-choose').css('display','none')
        $(this).data('clicked', false);
        $(this).removeClass(`item${count}`)
        if($(this).data('clicked', false))
        {   
            menu_list_classes = $(this).attr('class').split(' ')[$(this).attr('class').split(' ').length -1]
            $(`.choosen-item.${menu_list_classes}`).parents('.col-lg-6').remove()
            if(!$.trim( $(".choosen-items-container").html() ).length ){
                $('.choosen-items-container').css('display', 'none')
            }
            
        }
        total_price -= parseInt($(this).find('.menu-price-get span').text())
        console.log(total_price);
        $('.total-price').text(total_price)
        
    }
    else {   
       $(this).data('clicked', true);
       $(this).css('border', '2px solid #42FF00')
       $(this).siblings('.menu-item-choose').css('display','flex')
       
       
       total_price += parseInt($(this).find('.menu-price-get span').text())
       $('.total-price').text(total_price)
       choosen_item_box = $('<div class = "col-lg-6" ></div>') 
       choosen_item = $('<div></div>') 
       choosen_item.addClass(`card choosen-item item${count}`)
       meal_count = $('<div class=""></div>')
       decrease = $('<div></div>')
       decrease_btn = $('<button type="button" class="btn btn-outline-dark decrease-btn "></button>')
       decrease_btn_icon = $('<i class="fas fa-minus-circle"></i>')
       decrease.append(decrease_btn.append(decrease_btn_icon))
       decrease.addClass('decrease')
       menu_item_name = $('<div><h3 class="menu_item_name_header"></h3><span class="porsion" >1</span></div>')
       menu_item_name.addClass('menu-item-name')
       menu_item_name.find('.menu_item_name_header').text($(this).find('.menu-title-get').text())
       increase = $('<div></div>')
       increase_btn = $('<button type="button" class="btn btn-outline-dark increase-btn "></button>')
       increase_btn_icon = $('<i class="fas fa-plus-circle"></i>')
       increase.append(increase_btn.append(increase_btn_icon))
       increase.addClass('increase')
       dec_inc = $('<div class= "dec-inc"></div>') 
       dec_inc.append(decrease,increase)
       meal_count.append(menu_item_name,dec_inc)
       price = $('<div class="price"></div>')
       original_price = $('<span class="original-price">1</span>')
       menu_id = $('<span class="menu-id"></span>')
       price_span = $('<div class="justify-flex-end"><span class="dollar-sign">$</span><span class="price-span">1</span></div>')
       menu_id.text($(this).find('.menu-id').text())
       menu_id.css('display','none')
       price.append(original_price,menu_id,price_span)
       price_span.find('.price-span').text($(this).find('.menu-price-get span').text())
       
       meal_count.addClass('meal-count')
       decrease_btn.prop('disabled', true)
       decrease_btn.animate({opacity: 0.6}, 200)
       choosen_item.append(price,meal_count)
       choosen_item_box.append(choosen_item)
        $('.choosen-items-container').append(choosen_item_box)
        meal_pp = parseInt($(this).find('.menu-price-get span').text())
        price_span.parents('.choosen-item').find('.original-price').text(meal_pp)
        $(increase_btn).click(function(){

            meal_price = parseInt($(this).parents('.choosen-item').find('.price-span').text())
            meal_price += parseInt($(this).parents('.card').find('.original-price').text())
            $(this).parents('.choosen-item').find('.price-span').text(meal_price)
            $(this).parents('.meal-count').find('.porsion').text(meal_price/parseInt($(this).parents('.card').find('.original-price').text()))
            if(meal_price > parseInt($(this).parents('.card').find('.original-price').text())){
                $(this).parents('.dec-inc').find('.decrease-btn').prop('disabled', false)
                $(this).parents('.dec-inc').find('.decrease-btn').animate({opacity: 1}, 200)
            }
            
            total_price += parseInt($(this).parents('.card').find('.original-price').text())
            $('.total-price').text(total_price)
        })
        $(decrease_btn).click(function(){
            meal_price = parseInt($(this).parents('.choosen-item').find('.price-span').text())
            meal_price-= parseInt($(this).parents('.card').find('.original-price').text())
            console.log(meal_price)
            console.log(parseInt($(this).parents('.card').find('.original-price').text()))
            console.log('---------------')
            $(this).parents('.choosen-item').find('.price-span').text(meal_price)
            $(this).parents('.meal-count').find('.porsion').text(meal_price/parseInt($(this).parents('.card').find('.original-price').text()))
            if(meal_price == parseInt($(this).parents('.card').find('.original-price').text())){
                $(this).prop('disabled', true)
                $(this).animate({opacity: .6}, 200)
            }
            total_price -= parseInt($(this).parents('.card').find('.original-price').text())
            $('.total-price').text(total_price)
        })
      
    }
   
  })

  $('.table-images').click(function(){
      $('.table-images').animate({opacity: 1}, 200)
      $(this).animate({opacity: 0.6}, 200)
  })

 