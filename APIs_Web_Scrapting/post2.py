import requests
url="https://dihfahsih.com/api/reviews-list-secured/"
token="a847aa77929479dcf4ac15a3f5c71b28ea646771"
token_payload={
    'Authorization': f'Token {token}'
}
response=requests.get(url, headers=token_payload)
if response.status_code==201:
    data=response.json()
    print(data[:5])
else:
    print("failed to create a post")
    print("status code:", response.status_code)
    print("response:", response.text)
    
