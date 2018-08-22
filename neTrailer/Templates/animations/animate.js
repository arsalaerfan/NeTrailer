/*global skrollr */
/*global $ */
skrollr.init();

$(".logocon").click(function(){
  $("html, body").animate({ scrollTop: 100 });
});