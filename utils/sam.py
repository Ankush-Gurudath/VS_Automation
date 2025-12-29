from api_helpers import LytxApiClient

if __name__ == "__main__":
    username = "qa_ind_full_access"
    password = "Login123!"
    group_id = "2bb2d9b4-c801-e111-81ce-e61f13277aab"  # Replace with your group ID if needed
    vehicle_name = "QM408"  # Replace with your target vehicle name

    client = LytxApiClient(username, password)
    count = client.get_vehicle_count_by_vehicle_name(vehicle_name, group_id=group_id)
    print(f"Vehicle count for name '{vehicle_name}' in group '{group_id}': {count}")