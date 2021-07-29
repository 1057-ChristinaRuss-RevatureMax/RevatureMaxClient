/*
<td>Assessment label</td>
<td>Date</td>
<td>Score</td>
<td>Batch Average Score</td>
*/

function build_table(data){
	let thead_row = document.getElementById("stat_table_head");
	let columns = [];
	Object.keys(data).forEach(x=>{
		// use keys as column header names! fun!
		let td = document.createElement("td")
		td.textContent = x; //TODO maybe? make a dictionary that points from these names to names we want
		thead_row.appendChild(td);
		
		// pull out columns, we need rows later
		columns.push(data[x]);
	});

	//fill in table with "data"
	let endi = columns[0].length;
	let endj = columns.length;
	let tbody = document.getElementById("stat_table");
	for(i = 0; i < endi; i++){
		let tr = document.createElement("tr");
		tr.id = "row"+i;
		for(j = 0; j < endj; j++){
			let td = document.createElement("td")
			td.textContent = columns[j][i] // i & j swapped! we were given columns!
			tr.appendChild(td)
		}
		tbody.appendChild(tr);
	}
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
			graphIt(response_dict["chartData"]);
			build_table(response_dict["data"]);
		}
	})
}

/* the following is for testing purposes, remove when endpoint is mocked/ready... */
dict = {};
["label","date","score","batchAverage"].forEach(x=>{
	dict[x]=[];
	for(i = 0; i < 10; i++){
		dict[x].push("such a " + x + " " + i);
	};
});
build_table(dict);
