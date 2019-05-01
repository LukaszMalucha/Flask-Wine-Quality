
$('.dropdown-trigger').dropdown();


$(".alert-user").delay(3000).fadeOut(200, function() {
    $(this).alert('close');
});




$(document).ready(function() {

//  Mobile Menu
    $('.sidenav').sidenav();

//  Floating Button
    $('.fixed-action-btn').floatingActionButton({
        direction: 'left'
    });

    $('.tooltipped').tooltip();

//  Progress Bar

	var getMax = function() {
		return $(document).height() - $(window).height();
	}

	var getValue = function() {
		return $(window).scrollTop();
	}

	if ('max' in document.createElement('progress')) {
		var progressBar = $('progress');

		progressBar.attr({
			max: getMax()
		});

		$(document).on('scroll', function() {
			progressBar.attr({
				value: getValue()
			});
		});

		$(window).resize(function() {

			progressBar.attr({
				max: getMax(),
				value: getValue()
			});
		});

	}
	else {

		var progressBar = $('.progress-bar'),
			max = getMax(),
			value, width;

		var getWidth = function() {

			value = getValue();
			width = (value / max) * 100;
			width = width + '%';
			return width;
		}

		var setWidth = function() {
			progressBar.css({
				width: getWidth()
			});
		}

		$(document).on('scroll', setWidth);
		$(window).on('resize', function() {

			max = getMax();
			setWidth();
		});
	}
	//	Artificial Sommeliers

    $('#formRateWine').on('submit', function(event) {
        $.ajax({
            data: {
                fixed_acidity: $('#fixed_acidity').val(),
                volatile_acidity: $('#volatile_acidity').val(),
                citric_acid: $('#citric_acid').val(),
                residual_sugar: $('#residual_sugar').val(),
                chlorides: $('#chlorides').val(),
                free_sulfur_dioxide: $('#free_sulfur_dioxide').val(),
                total_sulfur_dioxide: $('#total_sulfur_dioxide').val(),
                density: $('#density').val(),
                pH: $('#pH').val(),
                sulphates: $('#sulphates').val(),
                alcohol: $('#alcohol').val()
            },
            type : 'POST',
            url: '/rate'

        })
        .done(function(data) {
            $('#rf-result').text(data.rf_predict),
            $('#gtb-result').text(data.gtb_predict),
            $('#vot-result').text(data.vot_predict),
            $('#rf-comment').text(data.random_forest_message),
            $('#gtb-comment').text(data.gradient_message),
            $('#vot-comment').text(data.vote_message)

        });

        event.preventDefault();


    });


});






