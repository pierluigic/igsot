
function get_timeseries() {
      var dataSet = [];
      axios.get('http://localhost:5000/query', {
		params: {
		      name : "infermiere"
		}
      }).then((response) => {
                       
                       const data = response.data;

				for (let i = 0; i < data.length; i++) {
				    dataSet.push(data[i]);
				}
				
			});
	return dataSet;
}


var options = {
          series: [],
          chart: {
          type: 'area',
          height: 350,
          stacked: true,
          events: {
            selection: function (chart, e) {
              console.log(new Date(e.xaxis.min))
            }
          },
        },
        colors: ['#008FFB', '#00E396', '#CED4DC'],
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'smooth'
        },
        fill: {
          type: 'gradient',
          gradient: {
            opacityFrom: 0.6,
            opacityTo: 0.8,
          }
        },
        legend: {
          position: 'bottom',
          horizontalAlign: 'left'
        },
        xaxis: {
          type: 'datetime'
        },
        };





