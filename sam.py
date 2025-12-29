import requests

# Step 1: Authenticate and get token
auth_url = "https://login.lytx.com/api/auth/user"
auth_data = {
    "username": "qa_ind_full_access",
    "password": "Login123!"
}
auth_response = requests.post(auth_url, json=auth_data)
auth_response.raise_for_status()
token = auth_response.json().get("access_token")  # Adjust key if token is under a different key
print("Access Token:", type(token))

# Step 2: Use token to call the devices API
api_url = "https://api.aws.drivecam.net/api/videosearch-api/devices"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
data = {
    "pageSize": 10,
    "groupIds": ["2bb2d9b4-c801-e111-81ce-e61f13277aab"],
    "vehicleIds": None,
    "serialNumbers": [None],
    "vehicleNames": [None],
    "sortType": "lastCommunicationDate",
    "sortDirection": "desc"
}
response = requests.post(api_url, headers=headers, json=data)
print(response.text)
response.raise_for_status()
item_count = response.json()["itemCount"]
print("itemCount from API:", item_count)
