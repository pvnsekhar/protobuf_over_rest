import requests
import calc_pb2


response=requests.get('http://127.0.0.1:5000/calc-data?var1=2&var2=358989',headers={'Content-Type': 'application/protobuf'})

# Deserialize the response
if response.status_code == 200:
    response_data = calc_pb2.calc_response()
    response_data.ParseFromString(response.content)
    print(f"Response: {response_data}")
else:
    print(f"Error: {response.status_code} - {response.text}")
