/*
<td>Assessment label</td>
<td>Date</td>
<td>Score</td>
<td>Batch Average Score</td>
*/

function build_row(i, row){
	let tbody = document.getElementById("stat_table");
	let tr = document.createElement("tr");
	tr.id = "row"+i;
	//TODO make sure these strings match the endpoint
	[
		"label",
		"date",
		"score",
		"batchAverage"
	].forEach(key=>{
		let td = document.createElement("td")
		td.textContent = row[key]
		tr.appendChild(td)
	});
	tbody.appendChild(tr);
}

function get_table(){
	let port = 5000;
	let host = "https://localhost";
	let endpoint = "/test/"; //TODO select endpoint for associate dashboard data
	let url = host + ':' + port + endpoint;
	fetch(url, {
		method: 'GET',
		mode: 'cors',
	}).then(response =>{
		console.log('reply:')
		console.log(response)
		return response.json()
	}).catch(err =>{
		console.log('mistakes were made:')
		console.log(err)
	}).then(response_dict =>{
/*
{
  "data": {
    [
      aColumn : [
        avalue0,
        avalue1,
        avalue2
      ],
      bColumn : [
        bvalue0,
        bvalue1,
        bvalue2
      ],
      cColumn : [...],
      dColumn : [...],
      eColumn : [...],
      fColumn : [...]
    ]
  },
  "chartData": {
  legend0: [
    Y0,
    Y0 + (0.33 * (Y3 - Y0)),
    Y0 + (0.66 * (Y3 - Y0)),
    Y3,
    Y4,
    Y4 + (0.5 * (Y6 - Y4)),
    Y6
  ],
  legend1: [...],
  legend2: [...]
  }
}
*/
		console.log('final step:')
		console.log(response_dict)
		console.log(typeof(response_dict))
	if (typeof(response_dict) != 'undefined'){
		//TODO change this to array version of forEach if necessary
		//call graphIt(response_dict["chartData"]);)
		Object.keys(response_dict).forEach(x=>{
			build_row(x, response_dict[x])
		})
	}
	})
}

/* the following is for testing purposes, remove when endpoint is mocked/ready... */
dict = {
	1:{
		"label": "such a label1"
		, "date": "such a date1"
		, "score": "such a score1"
		, "batchAverage": "such an average1"
	}
	,2:{
		"label": "such a label2"
		, "date": "such a date2"
		, "score": "such a score2"
		, "batchAverage": "such an average2"
	}
}

Object.keys(dict).forEach( x => { build_row(x, dict[x]) })
