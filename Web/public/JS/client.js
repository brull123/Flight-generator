var counter = 0;
const dep = document.getElementById("dep");
const arr = document.getElementById("arr");
const plane = document.getElementById("plane");
const min_dist = document.getElementById("min_dist");
const max_dist = document.getElementById("max_dist");

function request_flight() {
    console.log("Requesting flight");
    const dep_value = dep.value;
    const arr_value = arr.value;
    const plane_value = plane.value;
    const min_dist_value = min_dist.value;
    const max_dist_value = max_dist.value;
    const data = {dep_value, arr_value, plane_value, min_dist_value, max_dist_value};
    const options = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    }
    counter++;
    fetch("/api", options);
}