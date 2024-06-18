import requests

url = "http://jsonplaceholder.typicode.com/posts"

data = {
    "userId": 100000,
    "title": "Test",
    "body": "TestingApi post endpoint"
}

response = requests.post(url, json=data)

if response.status_code == 201:
    new_post = response.json()
    print("NEW POST CREATED: ", new_post)

else:
    print("Failed to create new post")
    

