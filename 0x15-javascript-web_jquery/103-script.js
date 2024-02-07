$(document).ready(function() {
	function fetchTranslation() {
		var languageCode = $("#language_code").val();
		var apiURL = "https://www.fourtonfish.com/hellosalut/hello/" + languageCode;
		$.get(apiURL, function(data) {
			$("#hello").text(data.hello);
		});
	}
	$("#btn_translate").click(fetchTranslation);
	$("#language_code").keypress(function(event) {
		if (event.keyCode === 13) {
			fetchTranslation();
		}
	});
});
