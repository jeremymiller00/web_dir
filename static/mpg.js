$(document).ready(function(){

    console.log('document is ready')

    $('#inference').click(async function(){ // get values from website
        console.log('button was clicked')
        const cylinders = parseFloat($('#cylinders').val());
        const horsepower = parseFloat($('#horsepower').val());
        const weight = parseFloat($('#weight').val());
        const data = {
            cylinders, horsepower, weight
        }
        console.log(data)
        const response = await $.ajax('/inference', {
            data: JSON.stringify(data),
            method: "post",
            contentType: "application/json"
        })
        console.log('response')
        $('#mpg').val(response.prediction) // gets prediction from model
    })

    $('#scatter-plot').click(async function(){
        console.log('scatter plot button was clicked')
        const response = await $.ajax('/plot')
        console.log('response')
        const mpg = response.map(a => a[0])
        const weight = response.map(a => a[1])
        console.log('mpg')
        // create the trace
        const trace = [{
            x:weight,
            y:mpg,
            mode:'markers',
            type:'scatter'
        }]
        // create the layout
        const layout = {
            xaxis:{
                title:'Weight'
            },
            yaxis:{
                title:'MPG'
            },
            title: 'Scatter MPG vs Weight',
            width: 800,
            height: 400
        }
        Plotly.plot($('#graph1')[0],trace,layout)
        $('#scatter-plot').hide()
    })

    $('#histogram-plot').click(async function(){
        console.log('histogram plot button was clicked')
        const response = await $.ajax('/plot')
        console.log('response')
        const mpg = response.map(a => a[0])
        // const weight = response.map(a => a[1])
        console.log('mpg')
        // create the trace
        const trace = [{
            x:mpg,
            type:'histogram'
        }]
        // create the layout
        const layout = {
            xaxis:{
                title:'MPG'
            },
            yaxis:{
                title:'Count'
            },
            title: 'Histogram MPG',
            width: 800,
            height: 400
        }
        Plotly.plot($('#graph2')[0],trace,layout)
        $('#histogram-plot').hide()
    })
})
