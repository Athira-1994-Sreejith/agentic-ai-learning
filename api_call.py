import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
response1 = requests.get("https://jsonplaceholder.typicode.com/users/1")
print(type(response))
print(response.status_code)
data = response.json()
print(response.text)
print(response.headers)
print(data)
data1=response1.json()
print(data1)
print("Name:", data1["name"])
print("Email:", data1["email"])
