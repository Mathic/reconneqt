var endpoint = 'api/chart/data'
var defaultData = []
var labels = []

// date picker
$('#date').datetimepicker({
  defaultDate: new Date(),
	timepicker:false,
	format:'m/d/Y',
  todayButton: true,
  prevButton: true,
  nextButton: true,
  defaultSelect: true,
	maxDate:'+1970/01/01', // and tommorow is maximum date calendar
});

var date = new Date();
$('#date').val((date.getMonth() + 1) + '/' + date.getDate() + '/' + date.getFullYear())

var chart = undefined;
var oldDate;

function hslToRgb(h, s, l){
  var r, g, b;

  if(s == 0){
    r = g = b = l; // achromatic
  }else{
    var hue2rgb = function hue2rgb(p, q, t){
      if(t < 0) t += 1;
      if(t > 1) t -= 1;
      if(t < 1/6) return p + (q - p) * 6 * t;
      if(t < 1/2) return q;
      if(t < 2/3) return p + (q - p) * (2/3 - t) * 6;
      return p;
    }

    var q = l < 0.5 ? l * (1 + s) : l + s - l * s;
    var p = 2 * l - q;
    r = hue2rgb(p, q, h + 1/3);
    g = hue2rgb(p, q, h);
    b = hue2rgb(p, q, h - 1/3);
  }

  return [Math.round(r * 255), Math.round(g * 255), Math.round(b * 255)];
}

var drawChart = function () {
  var coloR = [];
  var dynamicColors = function() {
    var rand = Math.floor(Math.random());
    var h = Math.random();
    var s = (25 + 70 * Math.random())/100;
    var l = (85 + 10 * Math.random())/100;
    var rgb = hslToRgb(h, s, l)
    return "rgb(" + rgb[0] + "," + rgb[1] + "," + rgb[2] + ")";
  };

  for (var i in defaultData) {
    coloR.push(dynamicColors());
  }

  var ctx = document.getElementById('motive-chart').getContext('2d');
  chart = new Chart(ctx, {
    type: 'horizontalBar',
    data: {
      labels: labels,
      datasets: [{
        label: "Motives",
        backgroundColor: coloR,
        borderColor: 'rgba(200, 200, 200, 1)',
        hoverBorderColor: 'rgba(200, 200, 200, 1)',
        data: defaultData,
      }]
    },
    // Configuration options go here
    options: {
      scales: {
        xAxes: [{
          ticks: {
              beginAtZero: true,
              stepSize: 1
          }
        }]
      }
    }
  });
}

if(chart == undefined){
  $.ajax({
    method: "GET",
    url: endpoint,
    success: function(data){
      // console.log(data)
      defaultData = data.default
      labels = data.labels
      if(defaultData.length == 0) {
        $('#motive-chart').hide()
      } else {
        $('#motive-chart').show()
        drawChart(defaultData.length)
        chart.update()
      }
    },
    error: function(error_data){
      console.log(error_data)
    }
  })
}

$('input.datepicker').on('change', function(){
  var currDate = this.value;
  if (currDate !== oldDate) {
    oldDate = currDate;
    $.ajax({
      type: "POST",
      url: endpoint,
      data: {
        date: $("#date").val().replace('//g', '-'),
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
      },
      context: this,
      success: function(data, status) {
        // console.log(data)
        defaultData = data.default
        labels = data.labels
        if(chart != undefined){
          chart.destroy()
        }
        if(defaultData.length == 0) {
          $('#motive-chart').hide()
        } else {
          $('#motive-chart').show()
          drawChart()
          chart.update()
        }
      }
    });

    $.ajax({
      type: "POST",
      url: $(this).attr('url'),
      data: {
        date: $("#date").val().replace('//g', '-'),
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
      },
      context: this,
      success: function(data, status) {
        $("#occurences").empty();
        $("#occurences").append($(data).find('#occurences').html());
        $("#progress-table").empty();
        $("#progress-table").append($(data).find('#progress-table').html());
      }
    });
  }
});
