
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










