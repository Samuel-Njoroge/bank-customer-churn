import requests
import json

# Replace with the actual scoring URI of your deployed model
scoring_uri = 'http://12d5c3fa-c3bc-4149-8d18-0e8014d2fb48.southafricanorth.azurecontainer.io/score'

# Encoded input data matching the expected feature order
input_data = json.dumps({
    "data": [
        # Customer 1 (encoded)
        [750, 0, 35, 1, 2, 80000.0, 1, 10, 5, 15000.0, 12000.0, 2, 0, 0],
        
        # Customer 2 (encoded)
        [640, 1, 45, 0, 1, 60000.0, 2, 15, 8, 5000.0, 20000.0, 3, 2, 1],
        
        # Customer 3 (encoded)
        [580, 0, 30, 2, 0, 40000.0, 0, 5, 3, 10000.0, 5000.0, 1, 1, 2]
    ]
})

# Set the content type to JSON as expected by the model
headers = {'Content-Type': 'application/json'}

# Send a POST request to the model's scoring URI
response = requests.post(scoring_uri, data=input_data, headers=headers)

# Print the response from the model
print(response.json())
