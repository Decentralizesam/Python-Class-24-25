import requests
# getting a url of an api end point 
url = "http://jsonplaceholder.typicode.com/posts"

# making a GET request to a server
response = requests.get(url)
# checking if the request was successful
if response.status_code == 200:
    # parse the json response data 
    data = response.json()
    print(data[0])

else:
    print("failed to retrieve json")


