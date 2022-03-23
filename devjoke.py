import requests

url = "https://backend-omega-seven.vercel.app/api/getjoke"

payload={}
headers = {
  'accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
