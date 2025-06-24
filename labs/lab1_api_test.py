import requests
url = “https://dog.ceo/api/breeds/image/random”
response = requests.get(url)
data = response.json()
print(“Here’s a random dog photo:”)
print(data[‘message’])
