const express = require('express')
const app = express();
var dep = null;
var arr = null;
var plane = null;
var min_dist = null;
var max_dist = null;


const port = 3000;

app.listen(port, () => console.log("Listening at port", port));
app.use(express.static("public"));
app.use(express.json());

app.post("/api", (request, response) => {
    console.log("I got a request");
    const data = request.body;

    dep = data.dep != "" ? data.dep : null;
    arr = data.arr != "" ? data.arr : null;
    plane = data.plane != "" ? data.plane : null;
    min_dist = data.min_dist != "" ? data.min_dist : null;
    max_dist = data.max_dist != "" ? data.max_dist : null;
    
    var data_array = [dep, arr, plane, min_dist, max_dist];
    for (i in data_array){
        console.log(data_array[i]);
    }
    response.json({
        "status":"success"
    })
});