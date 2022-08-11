from time import sleep
from bs4 import BeautifulSoup
import requests
import codecs
import json
url = "https://en.wikipedia.org/wiki/List_of_the_busiest_airports_in_Europe"

filename = "airports.txt"


def attempt_write(f, string):
    try:
        f.write(string + "|")
    except:
        pass


def load_from_wiki(allow_writing=False):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    # airports = soup.find_all("a")
    for i in soup.find_all("a", href=True):
        # for i in soup.find_all("a","mw-redirect", href=True):
        if allow_writing:
            f = codecs.open(filename, "a", "utf-8")

        if "Airport" in i.text or "Aeroporto" in i.text:
            try:
                country = i.parent.parent.find_all("a")[0].text
                airport = i.text
                print(airport, country)
                if allow_writing:
                    attempt_write(f, airport)
                    attempt_write(f, country)

                url_temp = "https://en.wikipedia.org{}".format(i['href'])
                result_temp = requests.get(url_temp)
                soup_temp = BeautifulSoup(result_temp.text, "html.parser")
                airport_icao = soup_temp.find_all("span", "nickname")

                airport_lat_list = soup_temp.find_all("span", "latitude")
                airport_lon_list = soup_temp.find_all("span", "longitude")

                if not airport_lon_list or not airport_lat_list:
                    airport_cord = soup_temp.find_all("td", "infobox-data")
                    for i in airport_cord:
                        if " N " in i.text or " E " in i.text or " W " in i.text or " S " in i.text:
                            coords = i.text.split(" ")
                            airport_lat = coords[0] + coords[1]
                            airport_lon = coords[2] + coords[3]
                else:
                    airport_lat = airport_lat_list[0].text
                    airport_lon = airport_lon_list[0].text

                for i in airport_icao:
                    if "ICAO" in i.parent.text:
                        a_icao = i.parent.text.split(":")[1].strip()
                        # print(a_icao)
                        if allow_writing:
                            attempt_write(f, a_icao)
                            attempt_write(f, airport_lat)
                            attempt_write(f, airport_lon)

                if allow_writing:
                    f.write("\n")
                    f.close()
                # print()
            except:
                break


def get_airlines():
    url = "https://en.wikipedia.org/wiki/Category:Lists_of_airlines_by_country"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    links = soup.find_all("a")
    lists = {}
    for i in links:
        if "List of airlines of" in i.text:
            country = i.text.split("List of airlines of ")[-1]
            print(country)
            airlines_output_list = []
            url_temp = "https://en.wikipedia.org{}".format(i['href'])
            result_temp = requests.get(url_temp)
            soup_temp = BeautifulSoup(result_temp.text, "html.parser")
            airlines = soup_temp.find_all("th", text="Airline\n")

            for j in airlines:
                airline_links = j.parent.parent.find_all("tr")
                for k in airline_links:
                    airline_item = k.find_all("td")
                    if airline_item:
                        airlines_output_list.append(airline_item[0].text.strip())
                    
            lists[country] = airlines_output_list
    x = json.dumps(lists, indent = 4, sort_keys=True)
    f = codecs.open("airlines.json", "w", "utf-8")
    f.write(x)

def delete_duplicates(filename):
    f = codecs.open(filename, "r", "utf-8")
    airports = []
    for i in f:
        if i not in airports:
            print(i.split("|")[-2])
            airports.append(i)
    f.close()
    f = codecs.open(filename, "w", "utf-8")
    for i in airports:
        f.write(i)


# load_from_wiki(True)
# delete_duplicates(filename)

get_airlines()
