import requests

url = "http://localhost:3838/"
wiki_link = "https://en.wikipedia.org/wiki/BMW"

response = requests.get(url, params={"link": wiki_link})

if response.status_code == 200:
    print(response.json())
    with open("infobox.json", "w") as outfile:
        outfile.write(response.text)

else:
    print(f"Request failed with status code {response.status_code}")
