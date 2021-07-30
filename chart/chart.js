//const dummyData = { 'associate': [0, 10, 20, 30, 40, 50, 60 ,70, 80, 90], 'batch':[0, 10, 30, 20, 40, 60, 50], 'henry':[100, 100, 100, 100, 100, 100, 100, 100]};
// function loadData() must be called after chart is declared in js file
// to change color of chart you only have change these color arrays
const fillColor = ['#72A4C299', '#FCB41499', '#F2692599'];
const lineColor = ['#72A4C2', '#FCB414', '#F26925'];

var ctx = document.getElementById('gradesChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data:{
        labels: ['Week 1', 'Week 2', 'Week 3', 'Week 3', 'Week 4', 'Week 5', 
            'Week 6', 'Week 7', 'Week 8', 'Week 9', 'Week 10', 'Week 11'],
        datasets: ""},
        
    options: {
        legend: {
            display: false
        },
        scales: {
            y: {
                beginAtZero: true,
            }
        }
    }
});


function loadData(dataList){
    var i = 0;
    for(label in dataList){
        let setLabel = label; // ledgend label
        let setData =  Object.values(dataList[label]);  // data to be graphed
        let setColor = fillColor[i]; // color of this datas background
        let setBorderColor = lineColor[i]; // color of ths datas trace
        let parsedData = {label: setLabel, data: setData, backgroundColor: setColor, borderColor: setBorderColor, borderWidth: 1, hidden: false,};
        
        myChart.data.datasets.push(parsedData);
        buildLegend(label, lineColor[i]);
        i++;
    };
    myChart.update();
}

function buildLegend(label, color){
    const legendChart = document.getElementById("chart-legend"); // This should be the container for the legend
    const legendItem = document.createElement('div');
    legendItem.setAttribute("class", "key-item");
    
    const button = document.createElement("button");
    button.onclick = function () { editChart(label)};
    legendItem.appendChild(button);
    button.style.backgroundColor = color;

    const labelTitle = document.createElement("p");
    labelTitle.innerHTML= label;
    labelTitle.onclick = function () { editChart(label)};
    legendItem.appendChild(labelTitle);

    legendChart.appendChild(legendItem);
}

function editChart(id){;
    myChart.data.datasets.forEach(function(ds) {
        if(ds.label == id)
            {ds.hidden = !ds.hidden;}
        console.log(id);
      });
        myChart.update();
}
