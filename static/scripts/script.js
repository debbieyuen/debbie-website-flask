// import { gsap } from "gsap";
// import { DrawSVGPlugin } from "gsap/DrawSVGPlugin";
// import flowers from 'home_images/debbie_flowers.svg'

// gsap.registerPlugin(DrawSVGPlugin);


$(function(){
    var $container = $('#Portfolio');
  
    $container.isotope({
      itemSelector: '.portfolio-item',
      layoutMode: 'masonry'
    }).css('overflow', 'auto');

    $container.imagesLoaded().progress( function() {
      $container.isotope('layout');
    });

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

    gsap.to(".sidebar", {duration: 1, x: 100});



    var slideIndex = 1;
    showSlides(slideIndex);
    
    // Next/previous controls
    function plusSlides(n) {
      showSlides(slideIndex += n);
    }
    
    // Thumbnail image controls
    function currentSlide(n) {
      showSlides(slideIndex = n);
    }
    
    function showSlides(n) {
      var i;
      var slides = document.getElementsByClassName("mySlides");
      var dots = document.getElementsByClassName("dot");
      if (n > slides.length) {slideIndex = 1}
      if (n < 1) {slideIndex = slides.length}
      for (i = 0; i < slides.length; i++) {
          slides[i].style.display = "none";
      }
      for (i = 0; i < dots.length; i++) {
          dots[i].className = dots[i].className.replace(" active", "");
      }
      slides[slideIndex-1].style.display = "block";
      dots[slideIndex-1].className += " active";
    }
