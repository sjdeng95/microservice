from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)

@app.route("/", methods=["GET"])

def handler():
    method = request.method
    if method != "GET":
        return jsonify({"error": f"Invalid request method. Expected GET, received {method}"}), 400

    link = request.args.get("link")
    if not link:
        return jsonify({"error": "No link provided"}), 400

    response = requests.get(link)
    
    if response.status_code != 200:
        return jsonify({"error": f"Failed to fetch data from {link}"}), 400

    res = infobox(link)    
    return jsonify(res)
   

def infobox(link):
    info_dict = {}
    req = requests.get(link)

    soup = BeautifulSoup(req.text, 'html.parser')

    info_table = soup.find('table', {'class': 'infobox'})
        
    for tr in info_table.find_all('tr'):
        if tr.find('th'):
            if tr.find('td').get_text() != "":
                key = tr.find('th').get_text(separator=' ').strip()
                value = tr.find('td').get_text(separator=' ').replace("\n"," ").strip().replace("  ",",").replace(" ,,",", ")
                info_dict[key] = value

    # json_object = json.dumps(info_dict, indent=4)
    return info_dict
        
        
if __name__ == "__main__":
    app.run(port=3838)
