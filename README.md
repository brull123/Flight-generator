<h1>Flight Generator</h1>

<h2>Description</h2>
Randomly generates departure and arrival airport, airline based on departure arrival country, airplane and amount of passengers.

<h2>Use</h2>
To generate a flight simply run flight_gen.py.

<h2>Options</h2>
The program offers several options:<br>
To set departure airport add --dep="DEPARTURE_AIRPORT_ICAO"<br>
To set arrival airport add --arr="ARRIVAL_AIRPORT_ICAO"<br>
To set airplane manually add --plane="AIRPLANE_CODE"<br>
All available airplanes and airports are in airplanes.json and airports.txt, airports.json is currently non functional<br>

Simple flight generator for simulation use only. Currently works for major airports in Europe only.