import requests


url = "https://webexapis.com/v1/rooms"

payload = {}
headers = {
  'Authorization': 'Bearer NjdhNjc3YmMtMjU2Zi00MTMyLWE4NzYtNjMwNmJlYzNhMjRiNjVkYTRiZTQtZmIz_PF84_consumer'
}

response = requests.request("GET", url, headers=headers, data = payload)
rooms = response.text

print(rooms)
