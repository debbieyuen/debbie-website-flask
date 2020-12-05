var container = $(".home_header")

gsap.to("div.home_header", {duration: 1, x: 100});

jQuery(document).ready(function(){
    $('h1').mousemove(function(e){
      var rXP = (e.pageX - this.offsetLeft-$(this).width()/2);
      var rYP = (e.pageY - this.offsetTop-$(this).height()/2);
      $('h1').css('text-shadow', +rYP/150+'px '+rXP/100+'px rgba(255,0,255,.8), '+rYP/150+'px '+rXP/70+'px rgba(255,237,0,1), '+rXP/100+'px '+rYP/150+'px rgba(0,255,255,.7)');
    });
 });