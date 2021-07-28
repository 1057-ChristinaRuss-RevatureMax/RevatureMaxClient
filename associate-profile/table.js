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
	let port = 5000
	let host = "https://localhost"
	let endpoint = "/test/"
	let url = host + ':' + port
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
		console.log('final step:')
		console.log(response_dict)
		console.log(typeof(response_dict))
	if (typeof(response_dict) != 'string'){
		//TODO change this to array version of forEach if necessary
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
