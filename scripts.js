$(document).ready(function(){
	// adds drop shadow to header if not at top
	$(window).scroll(function() {
		if ($(document).scrollTop() == 0) {
			$("#header").css({boxShadow: 'none'})
		} else {
			$("#header").css({boxShadow: '3px 0px 10px #AAAAAA'})
		}
	});
});
