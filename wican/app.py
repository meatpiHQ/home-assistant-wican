import time
import requests
import json
import os

# Path to options.json where the configuration is stored
OPTIONS_FILE = "/data/options.json"

# Load the options
with open(OPTIONS_FILE) as f:
    options = json.load(f)

# Get device IP and interval from options
device_ip = options.get("device_ip", "192.168.1.100")
interval_seconds = options.get("interval_seconds", 5)

# Main loop to send requests at the configured interval
while True:
    try:
        url = f"http://{device_ip}/status"
        print(f"Making HTTP request to {url}")
        response = requests.get(url)

        # Log the response
        print(f"Response: {response.status_code} - {response.text}")
        
    except Exception as e:
        print(f"Error during request: {e}")
    
    # Sleep for the configured interval
    time.sleep(interval_seconds)
