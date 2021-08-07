// This is where the javascript would go
// Select the elements that contains the tab
const tabs = document.querySelectorAll('[data-tab-target]');
const tabContent = document.querySelectorAll('[data-tab-content]');
// Loops through the elements every time it's click, show the content
tabs.forEach(tab => {
    tab.addEventListener('click', () =>{
        // Get the tab element dashboard, statistics, settings
        const target = document.querySelector(tab.dataset.tabTarget);
        // Remove active class
        tabContent.forEach(tabContent => {
            tabContent.classList.remove('active')
        });
        tabs.forEach(tab => {
            tab.classList.remove('active')
        });
        tab.classList.add("active");
        target.classList.add("active");
    });
});


// Instead of mockdata, we will be using a fetch request to call the endpoint from the Python Team
// Matthew Piazza knows more about this endpoint

// When we make a call to this endpoint, we will get back an email for each associate as well.
// For Python team to pull this data, we need to send them the batch ID we get from a cookie.

// To get the cookie, use document.cookie -- then we need to parse the cookie and pull the batch ID out. 

// javalin-cookie-store=eyJiYXRjaElEIjoiVFItMTAyMSJ9; batchID=TR-1021

let cookie = "javalin-cookie-store=eyJiYXRjaElEIjoiVFItMTAyMSJ9; batchID=TR-1021"

if (cookie.includes("batchID")){
    console.log(cookie.slice(cookie.search("batchID")))
}

// This is how we will parse the cookie so that we can return it in the fetch request


var mockdata = {0:{"Associate Name": ["BatchAverage", "name2", "name3"]},
                1:{"Quiz Score": ["77", "89", "34"]},
                2:{"Exam Score": ["34", "77", "89"]},
                3:{"Project Score": ["23", "77", "34"]},
                4:{"Verbal Score": ["55", "77", "22"]},
                5:{"Email": ["BATCH", "EMAIL1", "EMAIL2"]}}
// We need to convert the data to row format if possible

// build the table based on the mock data
// Need confirmation on how the data looks when I call the endpoint -- clarify with Matthew Piazza

function build_table(tabledata) {
	let columns = [];
    let emails = [];
    let thead = document.getElementById("associate-table-head")
    let tr = document.createElement("tr")
	Object.keys(tabledata).forEach(outer=>{
        Object.keys(tabledata[outer]).forEach(x=>{
            if(x != "Email"){
                console.log(x)
                let th = document.createElement("th")
                th.textContent = x;
                tr.appendChild(th);
                columns.push(tabledata[outer][x]);
            }
            else {
                console.log("I am inside the else")
                console.log(x)
                emails.push(tabledata[outer][x])
            }
        });
    });

    thead.appendChild(tr);
	console.log(emails)
	let endi = columns[0].length;
	let endj = columns.length;
    let btbody = document.getElementById("batch-table-head");
	let tbody = document.getElementById("associate-table-data");
    let flag = true
	for(i = 0; i < endi; i++){
        
		let tr = document.createElement("tr");
        console.log(emails[0][i])
        tr.setAttribute("onClick", "redirect(" +  "\"" + emails[0][i] + "\")")
        let btr = document.createElement("tr")
		tr.id = "row"+i;
		for(j = 0; j < endj; j++){
            if(i !== 0){
                
               
                let td = document.createElement("td")
			    td.textContent = columns[j][i] 
			    tr.appendChild(td)
            }
            else{
                let btd = document.createElement("td")
                btd.textContent = columns[j][i]
                btr.appendChild(btd)
            }
			
		}
        if(flag){
            btbody.appendChild(btr)
            flag = false;
        }
		tbody.appendChild(tr);
    };
    
}

build_table(mockdata)


function myFunction() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("searchBox");
    filter = input.value.toUpperCase();
    table = document.getElementById("associate-table");
    tr = table.getElementsByTagName("tr");
    console.log(tr)
    // Loop through all table rows, and hide those who don't match the search query
    //Add counter before the for loop 
    let count = 0;
    table.style.display = ""
    for (i = 1; i < tr.length; i++) {
      //for(j =0; j< tr[i].getElementsByTagName("td").length; j++){
      td = tr[i].getElementsByTagName("td")[0];
      console.log(td)
      // Try just grabbing the child element
      
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
          count++;
        } else {
          tr[i].style.display = "none";
        }
      }
    }
    if(count == 0){
        table.style.display = "none"
    }
    // If the counter is 0 after the for loop display none
  }


  function redirect(email) {
      window.location.href = "http://localhost/trainer-dashboard/" + email
  }