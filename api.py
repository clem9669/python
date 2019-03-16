import requests

#print ('Enter parameters lat & long: \n')
#

parameters = {"lat": 40.71, "lon": -74} #NYC


# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-pass.json",params=parameters)

#Print server status
print (response.status_code)

# Print the content of the response (the data the server returned)
print(response.content.decode("utf-8"))

# Print type of content we request
print(response.headers["content-type"])
