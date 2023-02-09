CS 361 - Assignment 8

Wikipedia Infobox Data Scraper Server Microservice

The server takes the link and parses together data from Wikipedia Tables with the HTML class name "infobox" and returns a JSON file of the parsed data.

How to Request Data From Server: 

    Send a HTTP GET request to the server with a link to a wikipedia article as a parameter. 

    Python Example: 

        import requests
        
        host = "http://localhost:3838/"

        parameters = {
            "link": "https://en.wikipedia.org/wiki/BMW"
        }
        # sending a request 
        requests.get(host, parameters)


How to Receive Data From Server:

    The server will respond to the request by sending a JSON Object of the parse wikipedia information. 

    The user will determine how to implement the JSON object. Example below prints and writes to a file.  

    Python Example: 

        # assign the return JSON object to a variable 
        response = requests.get(host, parameters)

        if response.status_code == 200:
            # print
            print(response.json())

            # write to file
            with open("infobox.json", "w") as outfile:
                outfile.write(response.text)


![Alt text](../Downloads/Untitled.jpg)

