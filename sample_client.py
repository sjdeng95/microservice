import requests

host = "http://localhost:3838/"

parameters = {
    "link": "https://en.wikipedia.org/wiki/BMW"
}

response = requests.get(host, parameters)

if response.status_code == 200:
    print(response.json())
    with open("infobox.json", "w") as outfile:
        outfile.write(response.text)

else:
    print(f"Request failed with status code {response.status_code}")
