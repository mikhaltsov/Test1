import requests
resp = requests.post('http://127.0.0.1:5000/similarity/api', json={"string1": "Hello world!", "string2": "Hello Dex Technologies!"})
print(resp.content)
