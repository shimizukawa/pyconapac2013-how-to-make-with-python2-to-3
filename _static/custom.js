$(function(){
	$('h2').each(function(i, elem){
		elem = $(elem);
		var page = elem.parent()
		var speech_elem = page.find('.speech');
		if(speech_elem.length != 0) {
			var hover = $('<span>').addClass('speech-hover').text('SP');
			$(document.body).mousemove(function(evt){
				if(
					hover.offset().left < evt.pageX &&
					hover.offset().left + hover.outerWidth() > evt.pageX &&
					hover.offset().top < evt.pageY &&
					hover.offset().top + hover.outerHeight() > evt.pageY) {
						speech_elem.css('top', evt.pageY - speech_elem.outerHeight());
						speech_elem.css('left', evt.pageX - page.offset().left);
						speech_elem.show();
				} else {
					speech_elem.hide();
				}
			});
			page.append(hover);
		}
	});
});
