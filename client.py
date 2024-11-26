import requests
import mydata_pb2

# Create and serialize Protobuf data
data = mydata_pb2.MyData(id="1", name="Client", age=30)
serialized_data = data.SerializeToString()

# Send HTTP POST request
response = requests.post('http://127.0.0.1:5000/send-data', data=serialized_data, headers={'Content-Type': 'application/protobuf'})

# Deserialize the response
if response.status_code == 200:
    response_data = mydata_pb2.MyData()
    response_data.ParseFromString(response.content)
    print(f"Response: {response_data}")
else:
    print(f"Error: {response.status_code} - {response.text}")
