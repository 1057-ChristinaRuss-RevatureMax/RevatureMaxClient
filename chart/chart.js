async function loadData(dataList){
    var chartData = [];
    const color = ['#eb4030', '#eb4030', '#eb4030'];
    const bColor = ['rgb(255, 99, 132)', 'rgb(255, 99, 132)', 'rgb(255, 99, 132)'];
    for(label in dataList){
        let i = 0;
        let setLabel = label; // ledgend label
        let setData =  Object.values(dataList[label]);  // data to be graphed
        let setColor = color[i]; // color of this datas background
        let setBorderColor = bColor[i]; // color of ths datas trace
        let parsedData = {label: setLabel, data: setData, backgroundColor: setColor, borderColor: setBorderColor, borderWidth: 1,};
        i++;
        chartData.push(parsedData);
    };
    return chartData;
}


async function graphIt(data){
    var Data = await loadData(data);
    var ctx = document.getElementById('gradesChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data:{
            labels: ['Week 1', 'Week 2', 'Week 3', 'Week 3', 'Week 4', 'Week 5', 
                'Week 6', 'Week 7', 'Week 8', 'Week 9', 'Week 10', 'Week 11'],
            datasets: Data,},
            
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
 }
