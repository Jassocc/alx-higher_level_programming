$(document).ready(function() {
	$("#btn_translate").click(function() {
		var languageCode = $("#language_code").val();
		var apiURL = "https://www.fourtonfish.com/hellosalut/hello/" + languageCode;
		$.get(apiURL, function(data) {
			$("#hello").text(data.hello);
		});
	});
});
