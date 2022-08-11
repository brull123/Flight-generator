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
    switch (data_response.status) {
        case "ok": {
            document.getElementById("result-dep").innerHTML = data_response.dep;
            document.getElementById("result-arr").innerHTML = data_response.arr;
            document.getElementById("result-airline").innerHTML = data_response.airline;
            document.getElementById("result-plane").innerHTML = data_response.plane;
            document.getElementById("result-pax").innerHTML = data_response.pax;
            document.getElementById("result-dist").innerHTML = data_response.dist;
            break;
        }
        case "error-dep": {
            const dep_error_el = document.getElementById("error-dep");
            dep_error_el.innerText = "Airport not in database";
            dep_error_el.style = "padding: 10px; padding-top: 10px; padding-bottom: 10px; padding-left: 10px; margin-top: 15px; margin-bottom: 5px; padding-right: 0px"
            break;
        }
        case "error-arr": {
            const dep_error_el = document.getElementById("error-arr");
            dep_error_el.innerText = "Airport not in database";
            dep_error_el.style = "padding: 10px; padding-top: 10px; padding-bottom: 10px; padding-left: 10px; margin-top: 15px; margin-bottom: 5px; padding-right: 0px"
            break;
        }
        case "error-plane": {
            const dep_error_el = document.getElementById("error-plane");
            dep_error_el.innerText = "Airplane not in database";
            dep_error_el.style = "padding: 10px; padding-top: 10px; padding-bottom: 10px; padding-left: 10px; margin-top: 15px; margin-bottom: 5px; padding-right: 0px"
            break;
        }
        case "error-min-dist": {
            const dep_error_el = document.getElementById("error-min-dist");
            dep_error_el.innerText = "Incorrect input";
            dep_error_el.style = "padding: 10px; padding-top: 10px; padding-bottom: 10px; padding-left: 10px; margin-top: 15px; margin-bottom: 5px; padding-right: 0px"
            break;
        }
        case "error-max-dist": {
            const dep_error_el = document.getElementById("error-max-dist");
            dep_error_el.innerText = "Incorrect input";
            dep_error_el.style = "padding: 10px; padding-top: 10px; padding-bottom: 10px; padding-left: 10px; margin-top: 15px; margin-bottom: 5px; padding-right: 0px"
            break;
        }
    }
}