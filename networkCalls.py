import requests 

URL = "https://jsonplaceholder.typicode.com/todos/1"

requestResult = requests.get(url = URL)

data = requestResult.json()

print(data)