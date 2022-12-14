# All airports information has been acquired from https://en.wikipedia.org/wiki/List_of_the_busiest_airports_in_Europe

import json
import random
import codecs
import math
import sys

max_distance = None
min_distance = None
short_plane_max_distance = 100
medium_plane_max_distance = 600


def load_airports_from_json():
    airports_list = []
    airports_filename = "airports.json"
    f = codecs.open(airports_filename, "r", "utf-8")
    airports_dict_list = json.loads(f.read())
    f.close()
    for i in airports_dict_list:
        tmp_airport = Airport()
        tmp_airport.decode_airport(i)
        airports_list.append(tmp_airport)

    return airports_list


class Airport:
    def __init__(self, name=None, country=None, ICAO=None, lat=None, lon=None):
        self.name = name
        self.country = country
        self.ICAO = ICAO
        self.lat = coords_to_number(lat) if lat is not None else None
        self.lon = coords_to_number(lon) if lon is not None else None

    def __repr__(self):
        lat_sign = "N" if self.lat >= 0 else "S"
        lon_sign = "E" if self.lon >= 0 else "W"
        return "{}, {}, {}, {}{:.2f}° {}{:.2f}°".format(self.ICAO, self.name, self.country, lat_sign, abs(self.lat), lon_sign, abs(self.lon))

    def distance_to(self, airport):
        lat1 = self.lat
        lon1 = self.lon
        lat2 = airport.lat
        lon2 = airport.lon

        R = 6371e3  # meters
        phi1 = lat1 * math.pi/180  # φ, λ in radians
        phi2 = lat2 * math.pi/180
        delta_phi = (lat2-lat1) * math.pi/180
        delta_lambda = (lon2-lon1) * math.pi/180

        a = math.sin(delta_phi/2) * math.sin(delta_phi/2) + math.cos(phi1) * \
            math.cos(phi2) * math.sin(delta_lambda/2) * \
            math.sin(delta_lambda/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        d = int(R * c * 0.000539956803)  # in nautical miles
        return d

    def encode_airport(self):
        return {"name": self.name, "country": self.country, "ICAO": self.ICAO, "lat": self.lat, "lon": self.lon}

    def decode_airport(self, airport_dict):
        self.name = airport_dict["name"]
        self.country = airport_dict["country"]
        self.ICAO = airport_dict["ICAO"]
        self.lat = airport_dict["lat"]
        self.lon = airport_dict["lon"]

    def find_suitable_airport(self, airport_list, min_distance, max_distance):
        airport_idx = random.randint(0, len(airport_list)-1)
        airport_2 = airport_list[airport_idx]

        max_search_cnt = 0
        while (max_distance is not None and airport_2.distance_to(self) > max_distance) or \
              (min_distance is not None and self.distance_to(airport_2) < min_distance) or self.ICAO == airport_2.ICAO:
            airport_idx = random.randint(0, len(airport_list)-1)
            airport_2 = airport_list[airport_idx]
            max_search_cnt += 1
            if max_search_cnt > len(airport_list):
                print("No suitable airport")
                exit()

        return airport_2


def generate(airport_list):
    dep = None
    arr = None
    min_distance = None
    max_distance = None

    for i in sys.argv:
        if "--dep" in i:
            dep_ICAO = i.split("=")[-1]
            for j in airport_list:
                if j.ICAO == dep_ICAO:
                    dep = j
                    break

    for i in sys.argv:
        if "--arr" in i:
            arr_ICAO = i.split("=")[-1]
            for j in airport_list:
                if j.ICAO == arr_ICAO:
                    arr = j
                    break

    for i in sys.argv:
        if "--min_dist" in i:
            min_distance = int(i.split("=")[-1].strip())
            break

    for i in sys.argv:
        if "--max_dist" in i:
            max_distance = int(i.split("=")[-1].strip())
            break

    if dep is None and arr is None:
        idx_dep = random.randint(0, len(airport_list)-1)
        dep = airport_list[idx_dep]
        arr = dep.find_suitable_airport(
            airport_list, min_distance, max_distance)

    elif arr is None:
        arr = dep.find_suitable_airport(
            airport_list, min_distance, max_distance)

    elif dep is None:
        dep = arr.find_suitable_airport(
            airport_list, min_distance, max_distance)

    dist = dep.distance_to(arr)
    print("Departure: ", end="")
    print(dep)
    print("Arrival: ", end="")
    print(arr)
    print("Distance: {} nm".format(dep.distance_to(arr)))
    return dep, arr, dist


def generate_airline(departure, arrival):
    with codecs.open("airlines.json") as f:
        data = json.load(f)
    country = [departure, arrival][random.randint(0, 1)]
    airline = data[country][random.randint(0, len(data[country])-1)]
    print("Airline:", airline)


def generate_pax(plane, planes_list):
    pax_lower_limit_numerator = 2
    pax_lower_limit_denominator = 3
    pax = None

    for i in planes_list:
        planes_list
        if plane in i:
            max_pax = i[-1]["pax"]
            break
    pax = random.randint((max_pax * pax_lower_limit_numerator) //
                         pax_lower_limit_denominator, max_pax)

    return pax


def generate_plane(distance=None):
    plane = None

    with codecs.open("airplanes.json") as f:
        data = json.load(f)
    planes_list = []

    for i in data:
        planes_list.append([i, data[i]])

    for i in sys.argv:
        if "--airplane" in i:
            plane = i.split("=")[-1]
            break

    if plane is None:
        plane = planes_list[random.randint(0, len(planes_list)-1)][0]
        plane_all = find_plane_in_list(plane, planes_list)
        desired_range = None
        if distance < short_plane_max_distance:
            desired_range = "short"
        elif distance < medium_plane_max_distance:
            desired_range = "medium"
        else:
            desired_range = "long"

        while plane_all[-1]["range"] != desired_range:
            plane = planes_list[random.randint(0, len(planes_list)-1)][0]
            plane_all = find_plane_in_list(plane, planes_list)

    pax = generate_pax(plane, planes_list)
    print("Plane:", plane)
    print("Passengers:", pax)


def find_plane_in_list(plane, planes_list):
    for i in planes_list:
        if i[0] == plane:
            return i


def coords_to_number(coord):
    if "S" in coord or "W" in coord:
        sign = -1
    else:
        sign = 1

    deg_rest = coord.split("°")
    deg = float(deg_rest[0])
    min_rest = deg_rest[1].split("′")
    mins = float(min_rest[0])
    secs = float(min_rest[1].split("″")[0])
    coord_number = sign * (deg + 1/60 * mins + 1/3600 * secs)
    return coord_number


airport_list = load_airports_from_json()
dep, arr, dist = generate(airport_list)
dep_country = dep.country
arr_country = arr.country
generate_airline(dep_country, arr_country)
generate_plane(dist)
