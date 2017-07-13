
$(document).ready(function(){
	resizeDiv();
	$("#coding").hover(
		
		function(){

			changeToHidden("bubbles");
			changeToVisible("myCanvas");
		}
	);
	$("#data_visualization").hover(
		
		function(){
			
			changeToHidden("myCanvas");
			changeToVisible("bubbles");
		}
	);
// document.ready finish
});

window.onresize = function(event) {
	resizeDiv();
}

function resizeDiv() {
	$("a.navbar-brand").css("margin-right", parseInt($(window).width())*0.4 + "px");
	$(".bubbleChart").css("max-width", parseInt($(window).innerWidth())*0.5 + "px");	
}


function changeToVisible(id) {
    var x = document.getElementById(id);
    if (x.style.visibility == 'hidden') {
        $("#"+id).css({opacity: 0.0, visibility: "visible"}).animate({opacity: 1.0}, 1200);
    } 
}

function changeToHidden(id) {
    var x = document.getElementById(id);
    if (x.style.visibility == 'visible') {
        x.style.visibility = 'hidden';
    }
}


