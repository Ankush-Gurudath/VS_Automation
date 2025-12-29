import requests
def get_api_vehicle_count(username, password):
    client = LytxApiClient(username, password)
    return client.get_vehicle_count()

class LytxApiClient:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.token = None
        self.authenticate()

    def authenticate(self):
        auth_url = "https://login.lytx.com/api/auth/user"
        auth_data = {
            "username": self.username,
            "password": self.password
        }
        auth_response = requests.post(auth_url, json=auth_data)
        auth_response.raise_for_status()
        self.token = auth_response.json().get("access_token")

    def get_vehicle_count(self, group_id="2bb2d9b4-c801-e111-81ce-e61f13277aab", page_size=10):
        api_url = "https://api.aws.drivecam.net/api/videosearch-api/devices"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        data = {
            "pageSize": page_size,
            "groupIds": [group_id],
            "vehicleIds": None,
            "serialNumbers": [None],
            "vehicleNames": [None],
            "sortType": "lastCommunicationDate",
            "sortDirection": "desc"
        }
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["itemCount"]
        
    def get_vehicle_count_by_vehicle_name(self, vehicle_name, group_id=None, page_size=10):
        """
        Get count of vehicles filtered by vehicle name
        
        Args:
            vehicle_name (str): Vehicle name to search for
            group_id (str, optional): Group ID to filter by
            page_size (int): Number of results per page
            
        Returns:
            int: Count of matching vehicles
        """
        api_url = "https://api.aws.drivecam.net/api/videosearch-api/devices"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        data = {
            "pageSize": page_size,
            "vehicleIds": None,
            "serialNumbers": [None],
            "vehicleNames": [vehicle_name],
            "sortType": "lastCommunicationDate",
            "sortDirection": "desc"
        }
        
        # Add group filter if provided 
        if group_id:
            data["groupIds"] = [group_id]
        else:
            data["groupIds"] = ["2bb2d9b4-c801-e111-81ce-e61f13277aab"]
            
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["itemCount"]
        
    def get_vehicle_count_by_serial_number(self, serial_number, group_id=None, page_size=10):
        """
        Get count of vehicles filtered by serial number
        
        Args:
            serial_number (str): Serial number to search for
            group_id (str, optional): Group ID to filter by
            page_size (int): Number of results per page
            
        Returns:
            int: Count of matching vehicles
        """
        api_url = "https://api.aws.drivecam.net/api/videosearch-api/devices"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        data = {
            "pageSize": page_size,
            "vehicleIds": None,
            "serialNumbers": [serial_number],
            "vehicleNames": [None],
            "sortType": "lastCommunicationDate",
            "sortDirection": "desc"
        }
        
        # Add group filter if provided
        if group_id:
            data["groupIds"] = [group_id]
        else:
            data["groupIds"] = ["2bb2d9b4-c801-e111-81ce-e61f13277aab"]
            
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["itemCount"]
