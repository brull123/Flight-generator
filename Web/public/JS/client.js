async function request_flight() {
    const dep_element = document.getElementById("dep");
    const arr_element = document.getElementById("arr");
    const plane_element = document.getElementById("plane");
    const min_dist_element = document.getElementById("min_dist");
    const max_dist_element = document.getElementById("max_dist");

    console.log("Requesting flight");

    const dep = dep_element.value != "" ? dep_element.value : "null";
    const arr = arr_element.value != "" ? arr_element.value : "null";
    const plane = plane_element.value != "" ? plane_element.value : "null";
    const min_dist = min_dist_element.value != "" ? min_dist_element.value : "null";
    const max_dist = max_dist_element.value != "" ? max_dist_element.value : "null";

    var data = { dep, arr, plane, min_dist, max_dist };

    const options = {
        method: "GET",
        headers: { "Content-Type": "application/json" }
        // body: JSON.stringify(data)
    }
    const base_url = "http://127.0.0.1:5000/";
    const api_url = `${base_url}api/${dep}/${arr}/${plane}/${min_dist}/${max_dist}`;
    console.log(api_url);

    const response = await fetch(api_url);
    var data_response = await response.json();

    console.log(data_response);
    document.getElementById("result-dep").innerHTML = data_response.dep;
    document.getElementById("result-arr").innerHTML = data_response.arr;
    document.getElementById("result-airline").innerHTML = data_response.airline;
    document.getElementById("result-plane").innerHTML = data_response.plane;
    document.getElementById("result-pax").innerHTML = data_response.pax;
    document.getElementById("result-dist").innerHTML = data_response.dist;
}