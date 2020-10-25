// import { gsap } from "gsap";
// import { DrawSVGPlugin } from "gsap/DrawSVGPlugin";
// import flowers from 'home_images/debbie_flowers.svg'

// gsap.registerPlugin(DrawSVGPlugin);


$(function(){
    var $container = $('#Portfolio');
  
    $container.isotope({
      itemSelector: '.portfolio-item',
      layoutMode: 'masonry',
      masonry: {
        columnWidth: 500
    }
    }).css('overflow', 'auto');
  
    $('#filters').on( 'click', 'a', function() {

      var filterValue = $(this).attr('data-filter');
      $('#filters a').removeClass('active');
      $(this).addClass('active');

      $container.isotope({ filter: filterValue });

    });
});



  $( document ).ready(function() {
  
    $(".menu_button").click(function(){
      $(".top_text").innerText = "email test"; 
      window.location = "/home";

    });
      $(".menu_button.button2").click(function(){
      window.location = "/portfolio";
    });
      $(".menu_button.button3").click(function(){
        window.location = "/research";
    });
  
    });

