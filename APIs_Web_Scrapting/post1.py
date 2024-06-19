import requests

url = "https://dihfahsih.com/api/review/"

# parameters 
# first_name 
# last_name
# relationship
# compliment

data = {
    "first_name" : "Ahmed",
    "last_name" : "Mohamed",
    "relationship" : "friend",
    "compliment" : "testing secured api call"
}
token = "a847aa77929479dcf4ac15a3f5c71b28ea646771"

token_payload={
    "authorization": f"token{token}"

}
response = requests.post(url, json=data,headers=token_payload)

if response.status_code == 201:
    new_post = response.json()
    print("NEW POST CREATED: ", new_post)

else:
    print("Failed to create new post")
    print("status code: ", response.status_code)
    print("Response: ", response.text)
