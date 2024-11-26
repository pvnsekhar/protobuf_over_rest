from flask import Flask, request, Response
import mydata_pb2

app = Flask(__name__)

@app.route('/send-data', methods=['POST'])
def send_data():
    try:
        # Deserialize Protobuf data from the request body
        received_data = mydata_pb2.MyData()
        received_data.ParseFromString(request.data)

        # Process the data
        print(f"Received: {received_data}")

        # Create a response
        response_data = mydata_pb2.MyData(id="123", name="Server", age=99)
        return Response(response_data.SerializeToString(), content_type='application/protobuf')
    except Exception as e:
        return str(e), 400

@app.route('/')
def hello():
    return "cool! it is working"

if __name__ == '__main__':
    app.run(debug=True)
