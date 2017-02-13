$(function() {
	$("a.gallery").fancybox();
	$(".main-nav .level1").click(function () {
		$(this).parent().toggleClass("active").siblings().removeClass('active');
		$(this).next().slideToggle().parent().siblings().children(".mainnav-dropmenu").hide();
		$(this).next().children().find(".mainnav-lvl3").hide();
		$(this).next().find(".active").removeClass('active');
	});
	$(".main-nav .level2").click(function () {
		$(this).parent().toggleClass("active").siblings().removeClass('active');
		$(this).next().slideToggle().parent().siblings().children(".mainnav-lvl3").hide();
	});
	$(".mob__menu").click(function () {
		$(this).parents(".main-nav").find(".mainnav-list").slideToggle();
	})

	$(".tovar__equipment .title").click(function () {
		$(this).parent().toggleClass("active").siblings().removeClass('active');
		$(this).parent().siblings().children("ul").hide();
		$(this).next().slideToggle();
	})
});
