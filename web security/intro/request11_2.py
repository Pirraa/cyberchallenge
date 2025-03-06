import requests

# URL endpoints
login_url = "http://web-11.challs.olicyber.it/login"
flag_piece_url = "http://web-11.challs.olicyber.it/flag_piece"

# Login credentials
credentials = {
    "username": "admin",
    "password": "admin"
}

# Create a session object to manage cookies
session = requests.Session()

# Perform login to get session cookie and CSRF token
response = session.post(login_url, json=credentials)
response_data = response.json()
csrf_token = response_data['csrf']

# Function to get flag piece by index
def get_flag_piece(index):
    headers = {
        "X-CSRF-Token": csrf_token
    }
    params = {
        "index": index
    }
    response = session.get(flag_piece_url, headers=headers, params=params)
    return response.text

# Retrieve all flag pieces
flag = ""
for i in range(4):
    flag += get_flag_piece(i)
    # Update CSRF token for the next request
    response_data = session.post(login_url, json=credentials).json()
    csrf_token = response_data['csrf']

print("Flag:", flag)